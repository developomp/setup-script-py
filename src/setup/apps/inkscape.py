from ..util import flatpak_install

name = "Inkscape"


def setup():
    """adobe illustrator but FOSS"""

    flatpak_install("org.inkscape.Inkscape")
