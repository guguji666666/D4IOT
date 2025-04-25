# D4IOT

## Switch users

| Current User     | Command                                            | Description (中文)                       | Description (English)                       |
|------------------|----------------------------------------------------|------------------------------------------|---------------------------------------------|
| admin            | ```bash system shell ```                           | 切换到 cyberx_host 用户                   | Switch to cyberx_host user                  |
| cyberx_host      | ```bash docker exec -it sensor<press tab> bash ```| 切换到 cyberx 用户                        | Switch to cyberx user                       |
| cyberx_host      | ```bash sudo su cyberx ```                        | 切换到 cyberx 用户                        | Switch to cyberx user                       |


## CLI Command List

| User           | Command                       | sudo Command                               | Command Syntax                                  | Operation Description (中文)             | Operation Description (English)         |
|----------------|-------------------------------|--------------------------------------------|-------------------------------------------------|------------------------------------------|-----------------------------------------|
| admin          | ```bash system```             | --                                         | ```bash cyberx-xsense-sanity```               | 检查系统状态                              | check sanity                           |
| system         | ```bash system sanity```      | --                                         | ```bash cyberx-xsense-sanity```               | 检查系统状态                              | check the system state                  |
| admin          | ```bash system reboot```      | ```bash sudo reboot```                     | ```bash sudo reboot```                         | 重启传感器                                | restart the sensor                      |
| cyberx_host    | ```bash system shutdown```    | ```bash sudo shutdown -r now```           | ```bash sudo shutdown -r now```              | 关闭传感器                                | shutdown the sensor                     |
| admin          | ```bash system version```     | --                                         | ```bash cyberx-xsense-version```              | 获取系统版本                              | get the system version                  |
| admin          | ```bash date```               | --                                         | ```bash date```                               | 获取系统日期和时间                        | get system date and time                |
| cyberx         | ```bash date```               | --                                         | ```bash date```                               | 获取系统日期和时间                        | get system date and time                |
| cyberx_host    | ```bash date```               | --                                         | ```bash date```                               | 获取系统日期和时间                        | get system date and time                |
| admin          | ```bash ntp enable```         | --                                         | ```bash cyberx-xsense-ntp-enable```          | 启用NTP时间同步                           | enable NTP for time sync                |
| admin          | ```bash ntp disable```        | --                                         | ```bash cyberx-xsense-ntp-disable```         | 禁用NTP时间同步                           | disable NTP for time sync                |
| backup         | ```bash system backup-list```  | --                                         | ```bash cyberx-xsense-system-backup-list```   | 列出所有可用备份                          | list all available backups on the sensor |
| backup         | ```bash system backup```       | --                                         | ```bash cyberx-xsense-system-backup -f <filename>``` | 创建传感器的备份                    | create a backup of the sensor            |
| backup         | ```bash system restore```      | --                                         | ```bash cyberx-xsense-system-restore```       | 从传感器备份恢复                          | restore from backups on the sensor       |
| backup         | ```bash --```                 | --                                         | ```bash cyberx-backup-memory-check```         | 检查备份空间分配                          | check how much space is allocated for backups |
| certificate     | ```bash --```                 | --                                         | ```bash cyberx-xsense-certificate-import```   | 导入证书                                  | import certificate                       |
| certificate     | ```bash --```                 | --                                         | ```bash cyberx-xsense-create-self-signed-certificate``` | 创建自签名证书                    | create a self-signed certificate        |
| network(24.1.5+) | ```bash network reconfigure```| --                                         | ```bash python3 -m cyberx.config.configure``` | 重新配置网络设置                          | reconfigure network settings             |
| network        | ```bash --```                 | ```bash sudo dpkg-reconfigure iot-sensor```| --                                              | 重新配置网络设置                          | reconfigure network settings             |
| network        | ```bash network validate```     | --                                         | --                                              | 验证并显示网络配置                        | validate and show network configuration   |
| network        | ```bash --```                 | --                                         | ```bash nload```                              | 显示不同接口的流量                        | show traffic on different interfaces     |
| network        | ```bash --```                 | --                                         | ```bash cyberx-xsense-internet-connectivity``` | 检查互联网连接                            | check internet connectivity               |
| network        | ```bash network list```       | --                                         | ```bash ifconfig```                           | 显示配置接口的状态                        | show status of configured interfaces      |
| network        | ```bash network capture-filter```| --                                       | ```bash cyberx-xsense-capture-filter```      | 配置捕获过滤器                            | configure capture filter                  |
| network        | ```bash --```                 | --                                         | ```bash cyberx-xsense-capture-filter -p all -m all-connected```| 重置捕获过滤器                          | reset capture filter                      |
| alerts         | ```bash --```                 | --                                         | ```bash cyberx-xsense-trigger-test-alert```  | 触发测试警报                              | trigger a test alert                     |
| alerts         | ```bash alerts exclusion-rule-list```| --                                     | ```bash alerts cyberx-xsense-exclusion-rule-list``` | 列出所有警报排除规则                  | list all alert exclusion rules           |
| alerts         | ```bash cyberx-xsense-exclusion-rule-create```| --                               | ```bash cyberx-xsense-exclusion-rule-create```| 创建新的警报排除规则                    | create new alert exclusion rule          |
| alerts         | ```bash exclusion-rule-append``` | --                                      | ```bash exclusion-rule-append```               | 修改警报排除规则                          | modify alert exclusion rule              |
| alerts         | ```bash exclusion-rule-remove``` | --                                      | ```bash exclusion-rule-remove```               | 删除警报排除规则                          | delete alert exclusion rule              |
| users          | ```bash --```                 | ```bash passwd```                        | ```bash cyberx-users-password-reset -u <user> -p <password>``` | 重置用户密码                              | reset user password                      |
| users          | ```bash logout```             | ```bash logout```                        | ```bash cyberx-xsense-logout```               | 退出用户                                  | log out of the user                     |
| admin          | ```bash timezone```            | --                                         | ```bash timezone```                            | 获取时区信息                              | get timezone information                  |


