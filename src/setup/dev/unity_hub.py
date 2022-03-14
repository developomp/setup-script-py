from src.util import flatpak_install

name = "Unity hub"
post_install = ["Change editors location"]


def setup():
    """Unity hub"""

    flatpak_install("com.unity.UnityHub")
