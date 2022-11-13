from src.util import flatpak_install

desc = "GNOME Calculator"


def setup():
    flatpak_install("org.gnome.Calculator")
