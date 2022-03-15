from src.util import flatpak_install

name = "steam"


def setup():
    """Game launcher"""

    flatpak_install("com.valvesoftware.Steam")
