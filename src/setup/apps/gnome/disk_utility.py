from src.util import paru_install

name = "GNOME Disk Utility"


def setup():
    """Disk management utility"""

    paru_install("gnome-disk-utility")
