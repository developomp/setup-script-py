from src.util import paru_install

name = "piper"


def setup():
    """gaming mouse configuration utility"""

    # Not using flatpak version because of some init bugs
    paru_install("piper")
