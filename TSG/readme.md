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

![image](https://github.com/user-attachments/assets/3336e50c-2a8b-40aa-9db9-7338f7e1e351)

![image](https://github.com/user-attachments/assets/d9e597ef-85ef-44f3-aac7-fafe9f85ff98)


## 3.Export logs via SFTP
### SFTP using `cyberx_host` account, navigate to path `/tmp`
![image](https://github.com/user-attachments/assets/6767b546-0218-4720-bd20-822ff6f041f1)



