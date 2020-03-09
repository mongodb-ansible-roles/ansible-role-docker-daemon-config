Ansible role for docker-daemon-config
==================================

An Ansible role for configuring the Docker daemon

![Test and Release](https://github.com/mongodb-ansible-roles/ansible-role-docker-daemon-config/workflows/Test%20and%20Release/badge.svg)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| docker_data_root | Root directory of persistent Docker state | `string` | `/var/lib/docker` | no |
| docker_debug | Enable debug mode | `bool` | `false` | no |
| docker_log_driver | Default driver for container logs | `string` | `json-file` | no |

Dependencies
------------

- [geerlingguy.docker](https://galaxy.ansible.com/geerlingguy/docker)

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-docker-daemon-config
```

License
-------

[Apache License](LICENSE)
