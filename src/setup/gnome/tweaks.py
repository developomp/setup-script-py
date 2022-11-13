from src.util import paru_install

desc = "Extra settings for GNOME"


def setup():
    paru_install("gnome-tweaks")
