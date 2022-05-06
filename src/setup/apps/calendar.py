from src.util import flatpak_install

name = "Calendar"


def setup():
    """GNOME calendar"""

    flatpak_install("org.gnome.Calendar")
