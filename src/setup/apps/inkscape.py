from src.util import flatpak_install

desc = "Adobe Illustrator but FOSS"


def setup():
    flatpak_install("org.inkscape.Inkscape")
