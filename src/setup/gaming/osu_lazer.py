from src.util import (
    paru_install,
    appimage_install,
    copy_file,
    get_latest_appimage_url_from_github,
)
from src.setup.system import system76_scheduler

from os import system


name = "osu!lazer"
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
    """
    A circle-clicking rhythm game.
    """

    # install the game
    appimage_install(
        get_latest_appimage_url_from_github("ppy/osu"),
        "osu",
    )

    # give CPU scheduler priority
    system76_scheduler.setup()
    setup_open_tablet_driver()
