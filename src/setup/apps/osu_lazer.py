from src.util import flatpak_install, paru_install, copy_file, run
from src.setup.system import system76_scheduler

from os.path import exists

name = "osu!lazer"
post_install = ["Install osu! skin from https://github.com/developomp/osu-pomp-skin"]


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
        run(
            f'sudo grep -qxF "blacklist {name}" /etc/modprobe.d/blacklist.conf || echo "blacklist {name}" | sudo tee -a /etc/modprobe.d/blacklist.conf'
        )

        # remove module from kernel if it's loaded
        run(f"sudo rmmod {name}")

    # Reload the systemd user unit daemon
    run("systemctl --user daemon-reload")

    # Enable and start the user service
    run("systemctl --user enable opentabletdriver --now")
