from src.constants import content_dir
from src.util import paru_install, copy_file

from os import makedirs

name = "Alacritty terminal"


def setup() -> None:
    """terminal app written in rust"""

    paru_install("alacritty")

    # copy configuration file
    copy_file(
        f"{content_dir}/home/pomp/.config/alacritty/alacritty.yml",
        "~/.config/alacritty/alacritty.yml",
    )
