from src.util import paru_install, copy_file

name = "Terminal"


def setup() -> None:
    """install and configure the kitty terminal"""

    paru_install(["kitty", "kitty-shell-integration"])

    # copy configuration file
    copy_file("home/.config/kitty/kitty.yml")
