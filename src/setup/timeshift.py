from src.util import paru_install

name = "timshift"


def setup():
    """System backup and restoring utility"""

    paru_install("timeshift")
