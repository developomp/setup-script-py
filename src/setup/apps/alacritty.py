from src.util import paru_install, copy_file

name = "Alacritty terminal"


def setup() -> None:
    """terminal app written in rust"""

    paru_install("alacritty")

    # copy configuration file
    copy_file("home/.config/alacritty/alacritty.yml")
