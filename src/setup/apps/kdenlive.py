from src.util import flatpak_install

desc = "Adobe Premiere Pro but FOSS"


def setup():
    flatpak_install("org.kde.kdenlive")
