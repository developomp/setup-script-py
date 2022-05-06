from src.util import flatpak_install

name = "Video player"


def setup():
    """GNOME video player"""

    flatpak_install("org.gnome.Totem")
