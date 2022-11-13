# https://github.com/tenacityteam/tenacity-flatpak-nightly

from os import system

desc = "Audacity fork that doesn't suck"


def setup():
    system(
        "flatpak remote-add tenacity oci+https://tenacityteam.github.io/tenacity-flatpak-nightly"
    )
    system("flatpak install tenacity org.tenacityaudio.Tenacity")
