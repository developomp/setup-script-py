from src.util import flatpak_install

name = "Blender"


def setup():
    """3D graphics tool"""

    flatpak_install("org.blender.Blender")
