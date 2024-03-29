from src.util import paru_install, flatpak_install, copy_file
from src.setup.system import system76_scheduler

from os import system


desc = "A circle-clicking rhythm game."
post_install = ["Install osu! skin from https://github.com/developomp/osu-pomp-skin"]


def setup_open_tablet_driver():
    paru_install("opentabletdriver-git")

    # apply settings
    copy_file("home/.config/OpenTabletDriver/settings.json")

    # disable built-in kernel modules
    modules_to_disable = [
        "wacom",
        "wacom_i2c",
        "wacom_w8001",
        "hid_uclogic",
    ]

    for name in modules_to_disable:
        # Add blacklist rule if it does not exist
        system(
            f'sudo grep -qxF "blacklist {name}" /etc/modprobe.d/blacklist.conf || echo "blacklist {name}" | sudo tee -a /etc/modprobe.d/blacklist.conf'
        )

        # remove module from kernel if it's loaded
        system(f"sudo rmmod {name}")

    # Reload the systemd user unit daemon
    system("systemctl --user daemon-reload")

    # Enable and start the user service
    system("systemctl --user enable opentabletdriver --now")


def setup():
    # setup tablet driver
    setup_open_tablet_driver()

    # install the game
    flatpak_install("sh.ppy.osu")

    # give CPU scheduler priority
    system76_scheduler.setup()
