import os

from src import log


def initialize():
    """
    Initialize before running any code.
    """

    log.log("Initializing flatpak")
    if os.system("sudo pacman -S --noconfirm --needed flatpak &> /dev/null"):
        log.error("Failed to install flatpak via pacman")
        exit(1)

    log.log("Initializing pip")
    if os.system("sudo pacman -S --noconfirm --needed python-pip &> /dev/null"):
        log.error("Failed to install pip via pacman")
        exit(1)

    # https://pypi.org/project/requests
    log.log("Initializing requests")
    if os.system("pip install requests &> /dev/null"):
        log.error("Failed to install requests via pip")
        exit(1)

    # https://pypi.org/project/PyYAML
    log.log("Initializing PyYAML")
    if os.system("pip install PyYAML &> /dev/null"):
        log.error("Failed to install PyYAML via pip")
        exit(1)

    # https://github.com/magmax/python-inquirer
    log.log("Initializing inquirer")
    if os.system("pip install inquirer &> /dev/null"):
        log.error("Failed to install inquirer via pip")
        exit(1)
