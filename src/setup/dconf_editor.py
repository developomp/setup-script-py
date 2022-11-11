from src.util import flatpak_install

name = "dconf editor"


def setup():
    """GUI application for editing dconf"""

    flatpak_install("ca.desrt.dconf-editor")
