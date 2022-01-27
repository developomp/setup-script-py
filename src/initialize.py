import os

from . import log


def initialize():
    """
    - install [pytermgui](https://github.com/bczsalba/pytermgui)
    """

    # Install flatpak
    if os.system("sudo pacman -S --noconfirm --needed flatpak &> /dev/null"):
        log.error("Failed to install flatpak")
        exit(1)

    # Install pip
    if os.system("sudo pacman -S --noconfirm --needed python-pip &> /dev/null"):
        log.error("Failed to install pip")
        exit(1)
