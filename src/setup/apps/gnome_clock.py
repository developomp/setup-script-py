from src.util import flatpak_install

name = "GNOME Clocks"


def setup():
    """For managing multiple time zone clocks."""

    flatpak_install("org.gnome.clocks")
