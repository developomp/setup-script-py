from ..util import flatpak_install

name = "osu!"


def setup():
    """Sucks all the joy out of your life but it's so fucking addictive"""

    flatpak_install("sh.ppy.osu")
