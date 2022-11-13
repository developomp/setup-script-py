from src.util import flatpak_install

desc = "FOSS game engine"


def setup():
    flatpak_install("org.godotengine.Godot")
