from src.util import paru_install, run


name = "rust"


def setup():
    """C++ but modern"""

    paru_install(["rustup", "rust-analyzer"])
    run("rustup install stable")
