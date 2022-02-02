from ...constants import tmp_dir
from ...util import pamac_install, smart_copy

from os import makedirs

name = "Alacritty terminal"


def setup() -> None:
    """terminal app written in rust"""

    pamac_install("alacritty")
    makedirs("~/.config/alacritty/")
    smart_copy(
        f"{tmp_dir}/home/pomp/.config/alacritty/alacritty.yml",
        "~/.config/alacritty/alacritty.yml",
    )
