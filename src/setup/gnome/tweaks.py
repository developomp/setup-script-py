from src.util import paru_install

name = "GNOME Tweaks"


def setup():
    """Extra settings for GNOME"""

    paru_install("gnome-tweaks")
