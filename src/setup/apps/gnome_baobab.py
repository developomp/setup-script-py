from src.util import flatpak_install

name = "Baobab"


def setup():
    """Storage usage analysis tool"""

    flatpak_install("org.gnome.baobab")
