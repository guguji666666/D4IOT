# Collect TSG logs from sensor

## 1.SSH to sensor using `cyberx` account
### [Access per privileged user](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/roles-on-premises#access-per-privileged-user)
![image](https://github.com/user-attachments/assets/2385be1b-7bca-4fee-b576-23e5a88ef388)

## 2. Creat bash script to collect logs
```sh
cd /opt && nano d4iot_tsg_logs.sh
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
    tar -cvf iottsglogs.tar "${existing_paths[@]}"
else
    echo "No valid paths to include in the tar file."
fi
```

![image](https://github.com/user-attachments/assets/a756b164-fdee-4750-a56f-d8f6540f83be)


Run the script
```sh
chmod +x d4iot_tsg_logs.sh
```
```sh
sh ./d4iot_tsg_logs.sh
```
