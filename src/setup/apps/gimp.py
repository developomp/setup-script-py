from src.util import flatpak_install

desc = "Photoshop but FOSS"


def setup():
    flatpak_install("org.gimp.GIMP")
