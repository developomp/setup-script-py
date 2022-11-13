from src.util import flatpak_install

desc = "Video player"


def setup():
    flatpak_install("org.gnome.Totem")
