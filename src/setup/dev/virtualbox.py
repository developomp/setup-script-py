from src.util import paru_install
from os import system

desc = "containerized OS"


def setup():
    paru_install(
        [
            "virtualbox",
            "virtualbox-host-modules-arch",
            "virtualbox-ext-oracle",
        ]
    )

    system("sudo systemctl enable systemd-modules-load")
    system("sudo systemctl start systemd-modules-load")
    system("sudo modprobe vboxdrv")
