from src.util import flatpak_install, paru_install, appimage_install, copy_file
from src.setup.system import system76_scheduler

from os.path import exists
from os import system
import requests
import re

name = "osu!lazer"
post_install = ["Install osu! skin from https://github.com/developomp/osu-pomp-skin"]


def get_latest_osu_lazer_appimage_url() -> str:
    return (
        re.search(
            "(?P<url>https?://[^\s]+)",
            [
                t
                for t in requests.get(
                    "https://api.github.com/repos/ppy/osu/releases/latest"
                ).text.split(",")
                if "browser_download" in t and 'AppImage"' in t
            ][0],
        )
        .group("url")
        .split(".AppImage")[0]
        + ".AppImage"
    )


def setup():
    """
    A circle-clicking rhythm game.
    """

    # install the game
    appimage_install(
        get_latest_osu_lazer_appimage_url(),
        "osu",
    )

    # give CPU scheduler priority
    system76_scheduler.setup()

    #
    # set up tablet driver
    #

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
