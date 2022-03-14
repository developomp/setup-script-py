from src.util import flatpak_install

name = "Godot"


def setup():
    """
    MIT licensed game engine

    check .zshrc for path stuff
    """

    flatpak_install("org.godotengine.Godot")
