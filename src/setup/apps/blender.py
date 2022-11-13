from src.util import flatpak_install

desc = "3D graphics tool"


def setup():
    flatpak_install("org.blender.Blender")
