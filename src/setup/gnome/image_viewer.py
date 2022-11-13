from src.util import flatpak_install

desc = "GNOME image viewing utility"


def setup():
    flatpak_install("org.gnome.eog")
