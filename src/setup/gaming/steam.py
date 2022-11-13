from src.util import flatpak_install

desc = "steam game downloader & launcher"


def setup():
    flatpak_install("com.valvesoftware.Steam")
