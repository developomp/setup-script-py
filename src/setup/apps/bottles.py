from src.util import flatpak_install

name = "bottles"


def setup():
    """wine bottle manager"""

    flatpak_install("com.usebottles.bottles")
