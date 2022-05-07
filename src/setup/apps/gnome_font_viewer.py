from src.util import flatpak_install

name = "GNOME font viewer"


def setup():
    """GNOME font viewer"""

    flatpak_install("org.gnome.font-viewer")
