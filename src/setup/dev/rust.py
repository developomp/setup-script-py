from src.util import paru_install
from os import system


desc = "C++ but modern"


def setup():
    paru_install(["rustup", "rust-analyzer"])
    system("rustup install stable")
