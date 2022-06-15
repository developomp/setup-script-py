from src.util import flatpak_install

name = "evince"


def setup():
    """Document viewer"""

    flatpak_install("org.gnome.Evince")
