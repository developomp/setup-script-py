from src.util import paru_install, run
from getpass import getuser

name = "Docker"


def setup():
    """Not a VM"""

    paru_install("docker")

    run(f'sudo usermod -aG docker "{getuser()}"')
    run("sudo systemctl --now enable docker")
