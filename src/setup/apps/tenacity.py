# https://github.com/tenacityteam/tenacity-flatpak-nightly

from src.util import run

name = "Tenacity"


def setup():
    """Safe audacity fork"""

    run(
        "flatpak remote-add tenacity oci+https://tenacityteam.github.io/tenacity-flatpak-nightly"
    )
    run("flatpak install tenacity org.tenacityaudio.Tenacity")
