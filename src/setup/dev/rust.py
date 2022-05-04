from src.util import paru_install
from os import system

name = "rust"


def setup():
    """The next C"""

    paru_install(["rust", "rustup"])

    system("rustup install stable")
