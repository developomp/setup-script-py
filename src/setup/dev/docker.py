from src.util import paru_install
from getpass import getuser
from os import system

name = "Docker"


def setup():
    """Not a VM"""

    paru_install("docker")

    system(f'sudo usermod -aG docker "{getuser()}"')
    system("sudo systemctl --now enable docker")
