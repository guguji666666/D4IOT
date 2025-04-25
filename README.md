# D4IOT

## CLI Command List

| User           | Command                       | sudo Command                               | Command Syntax                                 | Operation Description                   |
|----------------|-------------------------------|--------------------------------------------|------------------------------------------------|----------------------------------------|
| admin          | system                       | --                                         | cyberx-xsense-sanity                                      | check sanity (检查系统状态)            |
| system         | system sanity                | --                                         | cyberx-xsense-sanity                                      | 检查系统状态 (check the system state) |
| admin          | system reboot                | sudo reboot                                | sudo reboot                                       | restart the sensor (重启传感器)         |
| cyberx_host    | system shutdown              | sudo shutdown -r now                       | sudo shutdown -r now                              | shutdown the sensor (关闭传感器)         |
| admin          | system version               | --                                         | cyberx-xsense-version                                    | get the system version (获取系统版本)  |
| admin          | date                         | --                                         | date                                              | get system date and time (获取系统日期和时间) |
| cyberx         | date                         | --                                         | date                                              | get system date and time (获取系统日期和时间) |
| cyberx_host    | date                         | --                                         | date                                              | get system date and time (获取系统日期和时间) |
| admin          | ntp enable <IP address>     | --                                         | cyberx-xsense-ntp-enable <IP address>         | enable NTP for time sync (启用NTP时间同步) |
| admin          | ntp disable <IP address>    | --                                         | cyberx-xsense-ntp-disable                       | disable NTP for time sync (禁用NTP时间同步) |
| backup         | system backup-list           | --                                         | cyberx-xsense-system-backup-list                 | list all available backups on the sensor (列出所有可用备份) |
| backup         | system backup                | --                                         | cyberx-xsense-system-backup -f <filename>      | create a backup of the sensor (创建传感器的备份) |
| backup         | system restore               | --                                         | cyberx-xsense-system-restore                      | restore from backups on the sensor (从传感器备份恢复) |
| backup         | --                           | --                                         | cyberx-backup-memory-check                       | check how much space is allocated for backups (检查备份空间分配) |
| certificate    | --                           | --                                         | cyberx-xsense-certificate-import                 | import certificate (导入证书)           |
| certificate    | --                           | --                                         | cyberx-xsense-create-self-signed-certificate     | create a self-signed certificate (创建自签名证书) |
| network(24.1.5+)| network reconfigure         | --                                         | python3 -m cyberx.config.configure               | reconfigure network settings (重新配置网络设置) |
| network        | --                           | sudo dpkg-reconfigure iot-sensor           | --                                              | reconfigure network settings (重新配置网络设置) |
| network        | network validate             | --                                         | --                                              | validate and show network configuration (验证并显示网络配置) |
| network        | --                           | --                                         | nload                                           | show traffic on different interfaces (显示不同接口的流量) |
| network        | --                           | --                                         | cyberx-xsense-internet-connectivity             | check internet connectivity (检查互联网连接) |
| network        | network list                | --                                         | ifconfig                                        | show status of configured interfaces (显示配置接口的状态) |
| network        | network capture-filter       | --                                         | cyberx-xsense-capture-filter                    | configure capture filter (配置捕获过滤器) |
| network        | --                           | --                                         | cyberx-xsense-capture-filter -p all -m all-connected| reset capture filter (重置捕获过滤器) |
| alerts         | --                           | --                                         | cyberx-xsense-trigger-test-alert                | trigger a test alert (触发测试警报)     |
| alerts         | alerts exclusion-rule-list   | --                                         | alerts cyberx-xsense-exclusion-rule-list        | list all alert exclusion rules (列出所有警报排除规则) |
| alerts         | cyberx-xsense-exclusion-rule-create | --                                 | cyberx-xsense-exclusion-rule-create            | create new alert exclusion rule (创建新的警报排除规则) |
| alerts         | exclusion-rule-append        | --                                         | exclusion-rule-append                             | modify alert exclusion rule (修改警报排除规则) |
| alerts         | exclusion-rule-remove        | --                                         | exclusion-rule-remove                             | delete alert exclusion rule (删除警报排除规则) |
| users          | --                           | passwd                                     | cyberx-users-password-reset -u <user> -p <password> | reset user password (重置用户密码)    |
| users          | logout                       | logout                                     | cyberx-xsense-logout                             | log out of the user (退出用户)         |
| admin          | timezone                     | --                                         | timezone                                         | 获取时区信息                          |

表格已按您的要求更新，如果有其他命令需要添加或者有其他要求，请告诉我！
