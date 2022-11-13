from src.util import flatpak_install

desc = "GNOME character browser"


def setup():
    flatpak_install("org.gnome.Characters")
