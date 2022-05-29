from src.util import flatpak_install

name = "Kdenlive"


def setup():
    """FOSS video editing utility"""

    flatpak_install("org.kde.kdenlive")
