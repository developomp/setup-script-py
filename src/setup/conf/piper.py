from src.util import paru_install

desc = "Gaming mouse configuration utility"


def setup():
    # Not using flatpak version because of some init bugs
    paru_install("piper")
