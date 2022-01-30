from ..util import flatpak_install

name = "Godot"


def setup():
    """MIT licensed game engine"""

    flatpak_install("org.godotengine.Godot")
