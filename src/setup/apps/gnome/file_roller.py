from src.util import flatpak_install

name = "file roller"


def setup():
    """compression & decompression utility"""

    flatpak_install("org.gnome.FileRoller")
