# Step 1: Navigate to the target directory
# cd /home/cyber_host

# Step 2: Use a text editor to create the script file and add the content
cat << 'EOF' > microsoft_d4iot_tsg.sh
#!/bin/bash

# Script name: microsoft_d4iot_tsg.sh

# Purpose: This script creates a gzipped tar archive of specified directories under /opt/sensor,
#          with a filename that includes the current date and time in UTC.
# The script is designed to work with Microsoft's D4IoT system.

# Function to generate a timestamp in UTC
# The format YYYYMMDD_HHMMSS is used to ensure a unique and sortable identifier
generate_timestamp() {
    date -u +"%Y%m%d_%H%M%S"
}

# Generate the timestamp
TIMESTAMP=$(generate_timestamp)

# Name of the tar file
TAR_FILE="D4IOT_MS_TSG_${TIMESTAMP}.tar.gz"  # Add .gz to indicate compression

# List of paths to check and archive
paths=(
    "/opt/sensor/active/var/cyberx/logs"
    "/opt/sensor/active/var/logs"
    "/opt/sensor/logs"
)

# Initialize arrays for existing and missing paths
existing_paths=()  # Array to hold paths that exist
missing_paths=()   # Array to hold paths that do not exist

# Check each path for existence
for path in "${paths[@]}"; do
    if [ -e "$path" ]; then
        existing_paths+=("$path")  # Add to existing paths if found
    else
        missing_paths+=("$path")   # Add to missing paths if not found
    fi
done

# Output missing paths
if [ ${#missing_paths[@]} -ne 0 ]; then  # Check if there are missing paths
    echo "The following paths are missing:"
    for path in "${missing_paths[@]}"; do
        echo "$path"
    done
else
    echo "All paths exist."
fi

# Check disk space in /home/cyberx_host
DISK_SPACE=$(df -k /home/cyberx_host | awk 'NR==2 {print $4}')

if [ $DISK_SPACE -lt 100000 ]; then  # Less than 100MB free
    echo "Insufficient disk space in /home/cyberx_host. At least 100MB required."
    exit 1
fi

# Create a temporary directory
TEMP_DIR="/tmp/d4iot_ms_tsg_temp_${TIMESTAMP}"
sudo mkdir -p "$TEMP_DIR"

# Copy the existing paths to the temporary directory
for path in "${existing_paths[@]}"; do
    sudo cp -r "$path" "$TEMP_DIR/"
done

# Create gzipped tar file from the temporary directory
if sudo tar -cvzPf "/home/cyberx_host/${TAR_FILE}" -C "$TEMP_DIR" .; then
    echo "Gzipped tar file created: /home/cyberx_host/${TAR_FILE}"
else
    echo "Failed to create gzipped tar file. Check permissions or disk space."
    # Check if the tar file was partially created and remove it if so
    if [ -f "/home/cyberx_host/${TAR_FILE}" ]; then
        sudo rm "/home/cyberx_host/${TAR_FILE}"
        echo "Removed partially created gzipped tar file."
    fi
fi

# Remove the temporary directory
sudo rm -rf "$TEMP_DIR"
EOF

# Step 3: Make the script executable and run it
chmod +x microsoft_d4iot_tsg.sh
./microsoft_d4iot_tsg.sh
