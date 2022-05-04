from src.constants import content_dir
from src.util import flatpak_install, copy_file

from os import makedirs

name = "flatseal"


def setup() -> None:
    """flatpak permission manager"""

    flatpak_install("com.github.tchx84.Flatseal")
