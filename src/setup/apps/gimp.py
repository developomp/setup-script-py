from ...util import flatpak_install

name = "GIMP"


def setup():
    """photoshop but FOSS"""

    flatpak_install("org.gimp.GIMP")
