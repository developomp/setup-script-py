from src.util import flatpak_install

desc = "GNOME time management utility"


def setup():
    flatpak_install("org.gnome.clocks")
