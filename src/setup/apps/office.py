from src.util import flatpak_install

desc = "FOSS Office suite"


def setup():
    flatpak_install("org.onlyoffice.desktopeditors")
