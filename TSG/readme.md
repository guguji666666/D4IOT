# Collect TSG logs from sensor

## 1.SSH to sensor using `cyberx_host` account
### [Access per privileged user](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/roles-on-premises#access-per-privileged-user)
![image](https://github.com/user-attachments/assets/210042f5-3a3b-495b-aa68-89e9398a6f49)

## 2. Creat bash script to collect logs
```sh
cd && cd /tmp && nano d4iot_tsg_logs.sh
```

Save the context below
```sh
#!/bin/bash
# List of paths to check and archive
paths=(
    "/opt/sensor/active/var/cyberx/logs/azureiothub.log"
    "/var/cyberx/logs"
    "/opt/sensor/logs"
    "/opt/sensor/active/var/logs"
    "/var/host-logs"
    "/var/services-logs"
)
# Initialize arrays for existing and missing paths
existing_paths=()
missing_paths=()
# Check each path
for path in "${paths[@]}"; do
    if [ -e "$path" ]; then
        existing_paths+=("$path")
    else
        missing_paths+=("$path")
    fi
done
# Output missing paths
if [ ${#missing_paths[@]} -ne 0 ]; then
    echo "The following paths are missing:"
    for path in "${missing_paths[@]}"; do
        echo "$path"
    done
else
    echo "All paths exist."
fi
# Create tar file with existing paths
if [ ${#existing_paths[@]} -ne 0 ]; then
    tar -cvf iottsglogs.tar "${existing_paths[@]}" && echo "Tar file created: iottsglogs.tar"
else
    echo "No valid paths to include in the tar file."
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

![image](https://github.com/user-attachments/assets/6f42fadc-5e1e-4ae2-b23f-1bee413aecbc)

![image](https://github.com/user-attachments/assets/6d81556f-43f4-4584-965e-cbc5ec6e2331)


## 3.Export logs via SFTP
### SFTP using `cyberx` account
![image](https://github.com/user-attachments/assets/e5d5fde7-267c-474b-9b58-32ccc64be30f)


