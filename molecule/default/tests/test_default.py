import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_devops_file(host):
    f = host.file('/etc/sudoers.d/devops')

    assert f.exists
    assert f.contains('%devops ALL=(ALL:ALL) NOPASSWD: ALL')
    assert f.user == 'root'
    assert f.group == 'root'


def test_defaults_file(host):
    f = host.file('/etc/sudoers.d/defaults')

    assert f.exists
    assert f.contains('always_set_home')
    assert f.user == 'root'
    assert f.group == 'root'


def test_command_alias_file(host):
    f = host.file('/etc/sudoers.d/cmd_alias')

    assert f.exists
    assert f.contains('IPTABLES = /usr/bin/iptables -S')
    assert f.user == 'root'
    assert f.group == 'root'
