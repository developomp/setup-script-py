from ..util import pamac_install
from os import system

name = "virtualbox"


def setup():
    """It's a computer inside a computer!"""

    pamac_install([
        "virtualbox",
        "virtualbox-host-modules-arch",
        "virtualbox-ext-oracle"
    ])

    system("sudo systemctl enable systemd-modules-load")
    system("sudo systemctl start systemd-modules-load")
    system("sudo modprobe vboxdrv")
