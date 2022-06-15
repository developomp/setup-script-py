from src.util import flatpak_install

name = "cheese"


def setup():
    """photo/video utility"""

    flatpak_install("org.gnome.Cheese")
