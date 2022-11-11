from src.util import flatpak_install

name = "eye of gnome"


def setup():
    """photo viewing utility"""

    flatpak_install("org.gnome.eog")
