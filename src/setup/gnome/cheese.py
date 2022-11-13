from src.util import flatpak_install

desc = "GNOME photo taking utility"


def setup():
    flatpak_install("org.gnome.Cheese")
