from src.util import flatpak_install, paru_install

desc = "Screen recording and streaming utility"


def setup():
    flatpak_install("com.obsproject.Studio")
    paru_install("obs-plugin-input-overlay-bin")
