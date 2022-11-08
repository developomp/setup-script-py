from src.util import paru_install

name = "AppImage Launcher"


def setup():
    """Manages AppImage files"""

    paru_install("appimagelauncher")
