from src.util import flatpak_install

desc = "network analyzer"


def setup():
    flatpak_install("org.wireshark.Wireshark")
