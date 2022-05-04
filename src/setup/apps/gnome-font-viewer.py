from src.util import flatpak_install

name = "Gnome font viewer"


def setup():
    """Gnome font viewer"""

    flatpak_install("org.gnome.font-viewer")
