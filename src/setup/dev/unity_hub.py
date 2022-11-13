from src.util import flatpak_install

desc = "Unity version manager"
post_install = ["Change editors location"]


def setup():
    flatpak_install("com.unity.UnityHub")
