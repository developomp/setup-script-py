from src.util import flatpak_install

name = "GNOME Font Viewer"


def setup():
    """GNOME font viewing utility"""

    flatpak_install("org.gnome.font-viewer")
