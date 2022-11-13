from src.util import flatpak_install

desc = "GNOME compression & decompression utility"


def setup():
    flatpak_install("org.gnome.FileRoller")
