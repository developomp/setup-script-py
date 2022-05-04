from src.util import flatpak_install, paru_install

name = "OBS studio"


def setup():
    """
    Screen recording and streaming utility

    obs-plugin-input-overlay-bin: show inputs in OBS
    """

    flatpak_install("com.obsproject.Studio")

    paru_install("obs-plugin-input-overlay-bin")
