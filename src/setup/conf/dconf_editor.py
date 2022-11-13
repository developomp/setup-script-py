from src.util import flatpak_install

desc = "GUI application for editing dconf"


def setup():
    flatpak_install("ca.desrt.dconf-editor")
