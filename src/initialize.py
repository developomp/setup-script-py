from src.util import silent_system
from src import log


def install_via_pacman(package: str):
    log.log(f"Initializing {package}")
    if silent_system(f"paru -S --noconfirm {package}"):
        log.error(f"Failed to install {package} via pacman")
        exit(1)


def install_via_pip(package: str):
    log.log(f"Initializing {package}")
    if silent_system("pip install {package}"):
        log.error("Failed to install {package} via pip")
        exit(1)


def initialize():
    """
    Initialize before running any code.
    """

    install_via_pacman("flatpak")
    install_via_pacman("pip")

    install_via_pip("requests")
    install_via_pip("PyYAML")
    install_via_pip("inquirer")
