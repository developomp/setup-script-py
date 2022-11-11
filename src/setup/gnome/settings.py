from src.util import paru_install

name = "GNOME Control Center"


def setup():
    """The GNOME configuration utility"""

    paru_install("gnome-control-center")
