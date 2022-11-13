from src.util import flatpak_install

from os import makedirs

desc = "flatpak permission manager"


def setup() -> None:
    flatpak_install("com.github.tchx84.Flatseal")
