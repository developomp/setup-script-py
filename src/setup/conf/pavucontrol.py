from src.util import paru_install

name = "PulseAudio volume control"


def setup():
    """
    The thing I use until I find a good pipewire app
    """

    paru_install("pavucontrol")
