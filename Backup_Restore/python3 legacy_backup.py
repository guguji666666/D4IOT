#!/usr/bin/env python3

# Standard library imports
import argparse            # For command-line argument parsing
import os                  # For file and directory operations
import re                  # For regular expressions
import tempfile            # For creating temporary directories
import logging             # For logging debug/info messages
import tarfile             # For creating .tar/.gz archives
import sys                 # For manipulating system path and exit
import json                # For reading/writing JSON files
import math                # For working with infinite value
import shutil              # For high-level file operations
from subprocess import Popen, check_output  # For running shell commands

# Add sensor scripts path to Python path for importing custom modules
sys.path.append("/opt/sensor/active/scripts/")
from sensor_install_utils.creds_wrapper import CredentialsWrapper  # Custom wrapper to access stored credentials
from sensor_install_utils.properties import PropertiesWrapper      # Custom wrapper to read properties files

# Set up logger to output debug/info messages to console
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging

# Global constants
ACTIVE_DIR = "/opt/sensor/active"
FILTERED_PCAP_FILES_PATH = "/opt/sensor/persist/filtered-pcaps/"

# Load vulnerability assessment report directory from properties file
VA_CONFIG = os.path.join(ACTIVE_DIR, "proeprties/vulnerability-assessment.properties")
RISK_ASSESSMENT_FOLDER = PropertiesWrapper(VA_CONFIG).get('report.output.directory', "var/cyberx/reports/vulnerability-assessment")

# Cleanup directories (will be emptied during backup)
CLEANUP = ["var/cyberx/FSDumpDB/event_content_dictionary"]

# Volume backup list — currently empty, but meant for Docker volumes
VOLUME_BACKUP = []

# List of directories and files to include in the backup
SIMPLE_COPY_BACKUP = [
    { "name": "DATA_KEY", "src_folder": "etc/.system", "permissions": 0o755 },
    { "name": "properties", "src_folder": "var/cyberx/properties" },
    { "name": "configuration", "src_folder": "var/cyberx/configuration" },
    { "name": "datamining reports", "src_folder": "var/cyberx/media/presets" },
    { "name": "FSDump DB", "src_folder": "var/cyberx/FSDumpDB" },
    { "name": "risk assessment", "src_folder": RISK_ASSESSMENT_FOLDER },
    { "name": "scenarios properties", "src_folder": "var/cyberx/conf" },
    { "name": "cloud state", "src_folder": "var/cyberx/upgrade/cloudState" },
    { "name": "django secret key", "src_folder": "var/cyberx/keys/django-secret-key" },
    { "name": "signatures", "src_folder": "var/cyberx/signatures" },
    { "name": "active scans", "src_folder": "var/cyberx/active-scans" },
    { "name": "alert rules", "src_folder": "var/cyberx/alert_rules" },
    { "name": "licenses", "src_folder": "var/cyberx/licenses" },
    { "name": "certificates", "src_folder": "var/cyberx/keys/certificates" },
    { "name": "chrony", "src_folder": "etc/chrony" },
    { "name": "fluentd config", "src_folder": "etc/fluentd/env-config" },
    { "name": "proxy-certs", "src_folder": "var/cyberx/proxy-certs" },
    { "name": "wgetrc", "src_folder": "etc/wgetrc" },
    { "name": "squid", "src_folder": "etc/squid" },
    { "name": "site url", "src_folder": "var/cyberx/media/device-info/site_url.json" },
    { "name": "redis", "src_folder": "var/lib/redis/6379" },
    { "name": "mysql", "src_folder": "var/lib/mysql" }
]

# Copy files and directories while preserving ownership and permissions
def copy_with_save_owners_and_permissions(src, dst):
    logger.info(f"copying {src} -> {dst}")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    Popen(['cp', '-pLr', src, dst]).wait()  # cp with -p (preserve), -L (dereference symlinks), -r (recursive)

# Get folder size in KB using `du -d0`
def get_folder_size(path):
    res = check_output(f"du {path} -d0".split())  # -d0 gives only the total for the top-level dir
    return int(re.findall(r"\d+", res.decode())[0])  # Extract numeric result

# Query MySQL (inside Docker) for recent alert IDs with filtered PCAPs
def get_filtered_pcaps_ids(creds):
    username = creds['mysql.connection.username']
    password = creds['mysql.connection.password']
    containers = check_output("docker ps --format {{.Names}}".split()).decode()
    mariadb_container = re.findall("mariadb_.*", containers)[0]  # Find the running mariadb container
    query = ("SELECT id FROM CyberX.alerts "
             "WHERE last_occurence >= DATE(NOW() - INTERVAL 30 DAY) "
             "ORDER BY last_occurence DESC")
    query_cmd = f'/usr/bin/docker exec -i {mariadb_container} mysql -u {username} -p{password} -e '
    logger.info("Running pcap query in mysql")
    return check_output(query_cmd.split() + [query]).decode().split()[1:]  # Skip header row

# Copy filtered PCAPs based on IDs until disk budget is exhausted
def copy_filtered_pcaps(ids, target_directory, budget):
    while ids:
        alert_id = ids.pop(0)
        file_name = f"alert-{alert_id}.cap"
        pcap_src_path = os.path.join(FILTERED_PCAP_FILES_PATH, file_name)
        if not os.path.exists(pcap_src_path):
            logger.warn(f"Missing alert {pcap_src_path}")
            continue
        budget -= os.stat(pcap_src_path).st_size  # Subtract file size from remaining budget
        if budget < 0:
            logger.warn(f"Missing alerts {', '.join(ids)} and {alert_id}")
            break
        pcap_dst_path = os.path.join(target_directory, file_name)
        copy_with_save_owners_and_permissions(pcap_src_path, pcap_dst_path)

# Collect all backup data into target_dir
def collect_data(target_dir, creds):
    filtered_pcaps_ids = get_filtered_pcaps_ids(creds)  # Get alert PCAPs

    logger.info('Stopping Sensor')
    check_output("/bin/systemctl stop sensor-compose".split())  # Stop the sensor service

    # Cleanup empty directories
    for item in CLEANUP:
        path = os.path.join(ACTIVE_DIR, item)
        if os.path.exists(path):
            shutil.rmtree(path)
            os.mkdir(path)

    # Copy each backup item
    for item in SIMPLE_COPY_BACKUP:
        item_name = item.get("name")
        logger.info(f'backing up {item_name}')
        src_path = os.path.join(ACTIVE_DIR, item.get("src_folder"))
        dst_path = os.path.join(target_dir, item.get("src_folder"))
        copy_with_save_owners_and_permissions(src_path, dst_path)
        if "permissions" in item:
            os.chmod(dst_path, item.get("permissions"))

    # Copy Docker volumes (if defined)
    for item in VOLUME_BACKUP:
        item_name = item.get("name")
        logger.info(f'backing up volume {item_name}')
        src_path = f"/var/lib/docker/volumes/{item_name}/_data"
        dst_path = os.path.join(target_dir, item.get("target"))
        copy_with_save_owners_and_permissions(src_path, dst_path)

    # Copy filtered PCAPs with size limit
    budget = maximum_backup_size - get_folder_size(target_dir)
    if budget < 0:
        raise Exception("Backup too BIG")
    filtered_pcap_dst = os.path.join(target_dir, "var/cyberx/filtered-pcaps")
    copy_filtered_pcaps(filtered_pcaps_ids, filtered_pcap_dst, budget)

# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Legacy Backup')
    parser.add_argument('-s', '--size', type=int, required=False,
                        help='Total available disk space (in bytes) for the backup')
    parser.add_argument('-t', '--target', default="cyberx-system-backup.tar.gz",
                        help='Target backup file name')
    args = parser.parse_args()

    # Use provided size limit, or unlimited if not set
    maximum_backup_size = args.size or math.inf
    target_file = args.target

    with tempfile.TemporaryDirectory() as target_directory:
        # Retrieve MySQL credentials
        creds_wrapper = CredentialsWrapper()
        creds = { cred: creds_wrapper.get(cred) for cred in [
            "mysql.root.username",
            "mysql.connection.username",
            "mysql.root.password",
            "mysql.connection.password"
        ]}

        # Save credentials to file (used later during restoration)
        cred_file = os.path.join(target_directory, "credentials.json")
        with open(cred_file, "w") as f:
            json.dump(creds, f)

        # Use another temporary directory to hold original structure
        with tempfile.TemporaryDirectory() as tardir:
            os.chmod(tardir, 0o755)
            collect_data(tardir, creds)

            # Create a TAR file (not compressed yet)
            data_file = os.path.join(target_directory, "data.tar")
            with tarfile.open(data_file, "w") as tar:
                tar.add(tardir, arcname='.')

        # Copy version file into backup
        version_file = os.path.join(target_directory, "backup_version")
        copy_with_save_owners_and_permissions("/opt/sensor/active/version", version_file)

        # Compress everything into final target tar.gz
        logger.info('creating tar file in "{}"'.format(target_file))
        with tarfile.open(target_file, "w:gz") as tar:
            tar.add(target_directory, arcname='.')
