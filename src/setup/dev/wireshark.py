from src.util import flatpak_install

name = "Wireshark"


def setup():
    """network protocol analyzer GUI"""

    flatpak_install("org.wireshark.Wireshark")
