from src.util import flatpak_install

name = "GNOME Characters"


def setup():
    """Browser for emojis, special characters, and symbols."""

    flatpak_install("org.gnome.Characters")
