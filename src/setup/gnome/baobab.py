from src.util import flatpak_install

desc = "Disk usage analysis tool"


def setup():
    flatpak_install("org.gnome.baobab")
