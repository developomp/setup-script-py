from src.util import paru_install, run

name = "virtualbox"


def setup():
    """It's a computer inside a computer!"""

    paru_install(
        [
            "virtualbox",
            "virtualbox-host-modules-arch",
            "virtualbox-ext-oracle",
        ]
    )

    run("sudo systemctl enable systemd-modules-load")
    run("sudo systemctl start systemd-modules-load")
    run("sudo modprobe vboxdrv")
