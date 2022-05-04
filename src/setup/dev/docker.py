from src.util import paru_install
from os import system
from getpass import getuser

name = "Docker"


def setup():
    """Not a VM"""

    paru_install("docker")

    system(f'sudo usermod -aG docker "{getuser()}"')
    system("sudo systemctl --now enable docker")
