from src.util import pamac_install, copy_directory, remove_directory
from src.constants import content_dir

name = "polybar"


def setup():
    """Top bar thingy"""

    pamac_install(["polybar", "brightnessctl", "ttf-iosevka-nerd"])

    # remove existing files
    remove_directory("~/.config/polybar")

    # copy configs
    copy_directory(
        f"{content_dir}/home/pomp/.config/polybar/",
        "~/.config/",
    )
