from src.util import silent_system, paru_install
from src import log


def initialize():
    """
    Initialize before running any code.
    """

    log.log("Initializing flatpak")
    if paru_install("flatpak"):
        log.error("Failed to install flatpak via pacman")
        exit(1)

    log.log("Initializing pip")
    if paru_install("python-pip"):
        log.error("Failed to install pip via pacman")
        exit(1)

    # https://pypi.org/project/requests
    log.log("Initializing requests")
    if silent_system("pip install requests"):
        log.error("Failed to install requests via pip")
        exit(1)

    # https://pypi.org/project/PyYAML
    log.log("Initializing PyYAML")
    if silent_system("pip install PyYAML"):
        log.error("Failed to install PyYAML via pip")
        exit(1)

    # https://github.com/magmax/python-inquirer
    log.log("Initializing inquirer")
    if silent_system("pip install inquirer"):
        log.error("Failed to install inquirer via pip")
        exit(1)
