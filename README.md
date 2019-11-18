gabops.sudoers
==============
[![Build Status](https://travis-ci.org/gabops/ansible-role-sudo.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-sudo)
Installs and configures sudo

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| sudo_package | sudo | sudo package to install. |
| sudo_users | []] | List of usernames or %groupname. The configuration will be added in individual files using the value of `name` as filename. |
| sudo_defaults | [] | List of common defaults. |
| sudo_sudoers_defaults_file | ansible | The file where the common `sudo_defaults` will be written. |
| sudo_sudoers_d_path | /etc/sudoers.d | The path where all sudoers configuration files will be written. |
| sudo_command_alias_file | cmd_alias | The file where the command aliases defined in `sudo_command_alias` will be added. |
| sudo_command_alias | {} | A dict of command aliases that will be added to the file defined in `sudo_command_alias_file` |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: servers
      vars:
        sudo_defaults:
          - always_set_home
          - secure_path="/sbin:/bin:/usr/sbin:/usr/bin"
        sudo_users:
          - name: "%devops"
            nopasswd: true
            defaults: "!requiretty"
          - name: "%developers"
            commands:
              - /bin/ls
            command_alias:
              MYSQL_CONN: /usr/bin/mysql -h localhost -u developer -p
              APACHE: /usr/sbin/apachectl
          - name: "user1"
            commands:
              - /sbin/poweroff
              - IPTABLES
        sudo_command_alias:
          IPTABLES: /usr/bin/iptables -S
      roles:
         - role: sudo

```

License
-------

[License](./LICENSE)

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
