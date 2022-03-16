from src.constants import tmp_dir
from src.util import pamac_install, smart_copy

from os import makedirs

name = "Alacritty terminal"


def setup() -> None:
    """terminal app written in rust"""

    pamac_install("alacritty")

    # copy configuration file
    smart_copy(
        f"{tmp_dir}/home/pomp/.config/alacritty/alacritty.yml",
        "~/.config/alacritty/alacritty.yml",
    )
