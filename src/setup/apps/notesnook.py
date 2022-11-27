from src.util import flatpak_install

desc = "FOSS Note taking utility"


def setup():
    flatpak_install("com.notesnook.Notesnook")
