from src.util import paru_install
from os import system


name = "rust"


def setup():
    """C++ but modern"""

    paru_install(["rustup", "rust-analyzer"])
    system("rustup install stable")
