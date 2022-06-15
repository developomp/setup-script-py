from src.util import flatpak_install

name = "GNOME Logs"


def setup():
    """log viewer GUI"""

    flatpak_install("org.gnome.Logs")
