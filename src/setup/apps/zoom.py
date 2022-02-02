from ..util import flatpak_install

name = "Zoom"


def setup():
    """gay video conference app"""

    flatpak_install("us.zoom.Zoom")
