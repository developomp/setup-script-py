from src.util import flatpak_install

name = "Video player"


def setup():
    """gnome video player"""

    flatpak_install("org.gnome.Totem")
