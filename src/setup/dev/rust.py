from ...util import pamac_install
from os import system

name = "rust"


def setup():
    """The next C"""

    pamac_install(["rust", "rustup"])

    system("rustup install stable")
