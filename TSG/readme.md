# Collect TSG logs from sensor

## 1.SSH to sensor using `cyberx` account
### [Access per privileged user](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/roles-on-premises#access-per-privileged-user)
![image](https://github.com/user-attachments/assets/aac6174b-929c-433d-8791-b242c267c17d)


## 2. Verify the `core.log` and `core.err.log` exists
```sh
cd /var/cyberx/logs
```
![image](https://github.com/user-attachments/assets/2cc1bb09-3f4e-4608-923c-f4a7c4229835)

## 3. Copy the core.log and core.err.log logs
```sh
# Create the destination directory if it does not exist
mkdir -p /var/host-logs/iot_tsg_logs

# Copy the log files to the destination directory
cp /var/cyberx/logs/core.log /var/cyberx/logs/core.err.log /var/host-logs/iot_tsg_logs/
```

## 4. SSH to sensor using `cyberx_host` account
### [Access per privileged user](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/roles-on-premises#access-per-privileged-user)
![image](https://github.com/user-attachments/assets/3428d642-5b9e-4fb0-b2ee-a240c220d599)

Navigate to directory `/opt/sensor/logs`,  verify the directory `iot_tsg_logs` we created previously could be found
```sh
cd /opt/sensor/logs && ls -al
```
![image](https://github.com/user-attachments/assets/bc6fdf08-f070-4486-903f-67b1f0370422)


create bash script save the context below
```sh
nano collect_iot_logs.sh
```
```sh
#!/bin/bash

# List of paths to check and archive
paths=(
    "/opt/sensor/active/var/cyberx/logs/azureiothub.log"  # Specific log file path
    "/var/cyberx/logs"                                   # Directory containing logs
    "/opt/sensor/logs"                                   # Another directory for logs
    "/opt/sensor/active/var/logs"                        # Location for active logs
    "/var/host-logs"                                     # Host logs directory
    "/var/services-logs"                                 # Services logs directory
)

# Initialize arrays for existing and missing paths
existing_paths=()  # Array to hold paths that exist
missing_paths=()   # Array to hold paths that do not exist

# Check each path for existence
for path in "${paths[@]}"; do
    if [ -e "$path" ]; then                     # Check if the path exists
        existing_paths+=("$path")              # Add to existing paths if found
    else
        missing_paths+=("$path")                # Add to missing paths if not found
    fi
done

# Output missing paths
if [ ${#missing_paths[@]} -ne 0 ]; then            # Check if there are missing paths
    echo "The following paths are missing:"        # Output message for missing paths
    for path in "${missing_paths[@]}"; do
        echo "$path"                                # List each missing path
    done
else
    echo "All paths exist."                        # Confirmation message if all paths exist
fi

# Create tar file with existing paths
if [ ${#existing_paths[@]} -ne 0 ]; then            # Check if there are existing paths
    tar -cvf /opt/sensor/logs/iot_tsg_logs/iottsglogs.tar "${existing_paths[@]}" && \
    echo "Tar file created: /opt/sensor/logs/iot_tsg_logs/iottsglogs.tar"
else
    echo "No valid paths to include in the tar file."  # Message if no paths are valid
fi
```

![image](https://github.com/user-attachments/assets/e7ebef8c-dbc0-44c9-8d06-7d7fd58bd934)


Run the script
```sh
sudo chmod +x d4iot_tsg_logs.sh
```
```sh
sudo bash ./d4iot_tsg_logs.sh
```

![image](https://github.com/user-attachments/assets/3336e50c-2a8b-40aa-9db9-7338f7e1e351)

![image](https://github.com/user-attachments/assets/d9e597ef-85ef-44f3-aac7-fafe9f85ff98)


## 3.Export logs via SFTP
### SFTP using `cyberx_host` account, navigate to path `/tmp`
![image](https://github.com/user-attachments/assets/6767b546-0218-4720-bd20-822ff6f041f1)



