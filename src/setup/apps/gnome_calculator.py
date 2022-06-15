from src.util import flatpak_install

name = "GNOME Calculator"


def setup():
    """For calculating stuff"""

    flatpak_install("org.gnome.Calculator")
