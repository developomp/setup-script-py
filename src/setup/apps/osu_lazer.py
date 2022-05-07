from os.path import exists

from src.util import flatpak_install, paru_install
from src.setup.system import system76_scheduler

name = "osu!lazer"


def setup():
    """
    A circle-clicking rhythm game.
    """

    flatpak_install("sh.ppy.osu")
    system76_scheduler.setup()
