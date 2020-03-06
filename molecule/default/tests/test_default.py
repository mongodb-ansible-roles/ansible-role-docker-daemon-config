import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_host(host):
    assert host.file("/etc/docker/daemon.json").exists
    assert host.file("/var/lib/docker").exists
    # Ensure the handler restarted the Docker service
    assert host.service("docker").is_running
