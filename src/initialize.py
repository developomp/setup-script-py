import os

from . import log


def initialize():
    """
    Initialize before running any code.
    """

    log.log("Initializing flatpak")
    if os.system("sudo pacman -S --noconfirm --needed flatpak &> /dev/null"):
        log.error("Failed to install flatpak form archlinux package repository")
        exit(1)

    log.log("Initializing pip")
    if os.system("sudo pacman -S --noconfirm --needed python-pip &> /dev/null"):
        log.error("Failed to install pip from archlinux package repository")
        exit(1)

    # https://pypi.org/project/PyYAML
    log.log("Initializing PyYAML")
    if os.system("pip install PyYAML &> /dev/null"):
        log.error("Failed to install PyYAML from pip")
        exit(1)

    # https://github.com/bczsalba/pytermgui
    log.log("Initializing pytermgui")
    if os.system("pip install pytermgui &> /dev/null"):
        log.error("Failed to install pytermgui from pip")
        exit(1)
