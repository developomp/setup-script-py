from src.util import flatpak_install

name = "file roller"


def setup():
    """unzip thing"""

    flatpak_install("org.gnome.FileRoller")
