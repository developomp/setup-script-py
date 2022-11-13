from importlib.util import find_spec
from os import system

from src import log


def install_via_pacman_if_not_installed(package: str, test_command: str = ""):
    if test_command == "":
        test_command = package

    # Cannot use src.util.command_exists because some
    # python packages may not be installed yet.
    if not system(f"command -v {test_command} > /dev/null"):
        return

    if system(f"paru -S --noconfirm {package} > /dev/null"):
        log.error(f"Failed to install {package} via pacman")
        exit(1)


def install_via_pip_if_not_installed(package: str, package_import: str = ""):
    if package_import == "":
        package_import = package

    if find_spec(package_import):
        return

    if system(f"pip install {package} > /dev/null"):
        log.error(f"Failed to install {package} via pip")
        exit(1)


def initialize():
    """Make sure everything is prepared for the install scripts to run.
    You may assume Any function can be called after running this function."""

    install_via_pacman_if_not_installed("trash-cli", "trash-put")
    install_via_pacman_if_not_installed("flatpak", "flatpak")
    install_via_pacman_if_not_installed("python-pip", "pip")

    install_via_pip_if_not_installed("requests")
    install_via_pip_if_not_installed("PyYAML", "yaml")
    install_via_pip_if_not_installed("inquirer")
    install_via_pip_if_not_installed("tqdm")
