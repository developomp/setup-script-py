import os

from . import log


def initialize():
    """
    - install [pytermgui](https://github.com/bczsalba/pytermgui)
    - install pip
    """

    # Install flatpak
    if os.system("sudo pacman -S --noconfirm --needed flatpak"):
        log.error("Failed to install flatpak")
        exit(1)
