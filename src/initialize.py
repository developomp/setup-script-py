import os

from . import log


def initialize():
    """
    Initialize before running any code.
    """

    # Install flatpak
    if os.system("sudo pacman -S --noconfirm --needed flatpak &> /dev/null"):
        log.error("Failed to install flatpak form archlinux package repository")
        exit(1)

    # Install pip
    if os.system("sudo pacman -S --noconfirm --needed python-pip &> /dev/null"):
        log.error("Failed to install pip from archlinux package repository")
        exit(1)

    # install [pytermgui](https://github.com/bczsalba/pytermgui)
    if os.system("pip install pytermgui &> /dev/null"):
        log.error("Failed to install pytermgui from pip")
        exit(1)
