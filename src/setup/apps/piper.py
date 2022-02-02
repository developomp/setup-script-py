from ...util import flatpak_install

name = "piper"


def setup():
    """gaming mouse configuration utility"""

    flatpak_install("org.freedesktop.Piper")
