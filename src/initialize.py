from os import system
from src import log
from src.util import silent_system


def install_via_pacman(package: str):
    if silent_system(f"paru -S --noconfirm {package}", True):
        log.error(f"Failed to install {package} via pacman")
        exit(1)


def install_via_pip(package: str):
    if silent_system(f"pip install {package}"):
        log.error(f"Failed to install {package} via pip")
        exit(1)


def initialize():
    """Make sure everything is prepared for the install scripts to run.
    You may assume Any function can be called after running this function."""

    print("Initializing...")

    install_via_pacman("trash-cli")
    install_via_pacman("flatpak")
    install_via_pacman("python-pip")

    install_via_pip("requests")
    install_via_pip("PyYAML")
    install_via_pip("inquirer")
