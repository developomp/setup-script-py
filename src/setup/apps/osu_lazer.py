from os.path import exists
from os import system

from src.constants import content_dir, home_dir
from src.util import flatpak_install, paru_install, copy_file, silent_system
from src.setup.system import system76_scheduler

name = "osu!lazer"


def setup():
    """
    A circle-clicking rhythm game.
    """

    # install the game
    flatpak_install("sh.ppy.osu")

    # give CPU scheduler priority
    system76_scheduler.setup()

    #
    # set up tablet driver
    #

    paru_install("opentabletdriver-git")

    # apply settings
    copy_file(
        f"{content_dir}{home_dir}/.config/OpenTabletDriver/settings.json",
        "~/.config/OpenTabletDriver/settings.json",
    )

    # disable built-in kernel modules
    modules_to_disable = [
        "wacom",
        "wacom_i2c",
        "wacom_w8001",
        "hid_uclogic",
    ]

    for name in modules_to_disable:
        # Add blacklist rule if it does not exist
        silent_system(
            f'sudo grep -qxF "blacklist {name}" /etc/modprobe.d/blacklist.conf || echo "blacklist {name}" | sudo tee -a /etc/modprobe.d/blacklist.conf'
        )

        # remove module from kernel if it's loaded
        silent_system(f"sudo rmmod {name}")

    # Reload the systemd user unit daemon
    system("systemctl --user daemon-reload")

    # Enable and start the user service
    system("systemctl --user enable opentabletdriver --now")
