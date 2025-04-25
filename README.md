# D4IOT

## Switch users

| Current User     | Command                                            | Description (中文)                       | Description (English)                       |
|------------------|----------------------------------------------------|------------------------------------------|---------------------------------------------|
| admin            | system shell                                       | 切换到 cyberx_host 用户                   | Switch to cyberx_host user                  |
| cyberx_host      | docker exec -it sensor<press tab> bash            | 切换到 cyberx 用户                        | Switch to cyberx user                       |
| cyberx_host      | sudo su cyberx                                    | 切换到 cyberx 用户                        | Switch to cyberx user                       |

如果你有其他修改意见，请告诉我！

## CLI Command List

| User           | Command                       | sudo Command                               | Command Syntax                                  | Operation Description (中文)             | Operation Description (English)         |
|----------------|-------------------------------|--------------------------------------------|-------------------------------------------------|------------------------------------------|-----------------------------------------|
| admin          | system                        | --                                         | cyberx-xsense-sanity                           | 检查系统状态                              | check sanity                           |
| system         | system sanity                 | --                                         | cyberx-xsense-sanity                           | 检查系统状态                              | check the system state                  |
| admin          | system reboot                 | sudo reboot                                | sudo reboot                                     | 重启传感器                                | restart the sensor                      |
| cyberx_host    | system shutdown               | sudo shutdown -r now                       | sudo shutdown -r now                            | 关闭传感器                                | shutdown the sensor                     |
| admin          | system version                | --                                         | cyberx-xsense-version                          | 获取系统版本                              | get the system version                  |
| admin          | date                          | --                                         | date                                            | 获取系统日期和时间                        | get system date and time                |
| cyberx         | date                          | --                                         | date                                            | 获取系统日期和时间                        | get system date and time                |
| cyberx_host    | date                          | --                                         | date                                            | 获取系统日期和时间                        | get system date and time                |
| admin          | ntp enable                    | --                                         | cyberx-xsense-ntp-enable                       | 启用NTP时间同步                           | enable NTP for time sync                |
| admin          | ntp disable                   | --                                         | cyberx-xsense-ntp-disable                      | 禁用NTP时间同步                           | disable NTP for time sync                |
| backup         | system backup-list            | --                                         | cyberx-xsense-system-backup-list               | 列出所有可用备份                          | list all available backups on the sensor |
| backup         | system backup                 | --                                         | cyberx-xsense-system-backup -f <filename>     | 创建传感器的备份                          | create a backup of the sensor             |
| backup         | system restore                | --                                         | cyberx-xsense-system-restore                   | 从传感器备份恢复                          | restore from backups on the sensor       |
| backup         | --                            | --                                         | cyberx-backup-memory-check                     | 检查备份空间分配                          | check how much space is allocated for backups |
| certificate     | --                            | --                                         | cyberx-xsense-certificate-import               | 导入证书                                  | import certificate                       |
| certificate     | --                            | --                                         | cyberx-xsense-create-self-signed-certificate   | 创建自签名证书                            | create a self-signed certificate        |
| network(24.1.5+)| network reconfigure          | --                                         | python3 -m cyberx.config.configure             | 重新配置网络设置                          | reconfigure network settings             |
| network        | --                            | sudo dpkg-reconfigure iot-sensor          | --                                              | 重新配置网络设置                          | reconfigure network settings             |
| network        | network validate              | --                                         | --                                              | 验证并显示网络配置                        | validate and show network configuration   |
| network        | --                            | --                                         | nload                                          | 显示不同接口的流量                        | show traffic on different interfaces     |
| network        | --                            | --                                         | cyberx-xsense-internet-connectivity            | 检查互联网连接                            | check internet connectivity               |
| network        | network list                 | --                                         | ifconfig                                       | 显示配置接口的状态                        | show status of configured interfaces      |
| network        | network capture-filter        | --                                         | cyberx-xsense-capture-filter                   | 配置捕获过滤器                            | configure capture filter                  |
| network        | --                            | --                                         | cyberx-xsense-capture-filter -p all -m all-connected| 重置捕获过滤器                          | reset capture filter                      |
| alerts         | --                            | --                                         | cyberx-xsense-trigger-test-alert              | 触发测试警报                              | trigger a test alert                     |
| alerts         | alerts exclusion-rule-list    | --                                         | alerts cyberx-xsense-exclusion-rule-list       | 列出所有警报排除规则                      | list all alert exclusion rules           |
| alerts         | cyberx-xsense-exclusion-rule-create| --                                   | cyberx-xsense-exclusion-rule-create            | 创建新的警报排除规则                      | create new alert exclusion rule          |
| alerts         | exclusion-rule-append         | --                                         | exclusion-rule-append                           | 修改警报排除规则                          | modify alert exclusion rule              |
| alerts         | exclusion-rule-remove         | --                                         | exclusion-rule-remove                           | 删除警报排除规则                          | delete alert exclusion rule              |
| users          | --                            | passwd                                     | cyberx-users-password-reset -u <user> -p <password> | 重置用户密码                              | reset user password                      |
| users          | logout                        | logout                                     | cyberx-xsense-logout                           | 退出用户                                  | log out of the user                     |
| admin          | timezone                      | --                                         | timezone                                        | 获取时区信息                              | get timezone information                  |

请告诉我是否需要进一步的修改或添加！
