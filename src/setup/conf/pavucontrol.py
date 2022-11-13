from src.util import paru_install

desc = "PulseAudio manager"


def setup():
    paru_install("pavucontrol")
