# https://github.com/tenacityteam/tenacity-flatpak-nightly

from os import system

name = "Tenacity"


def setup():
    """Safe audacity fork"""

    system("flatpak remote-add tenacity oci+https://tenacityteam.github.io/tenacity-flatpak-nightly")
    system("flatpak install tenacity org.tenacityaudio.Tenacity")
