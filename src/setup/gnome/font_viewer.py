from src.util import flatpak_install

desc = "GNOME font viewing utility"


def setup():
    flatpak_install("org.gnome.font-viewer")
