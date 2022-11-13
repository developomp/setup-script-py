from src.util import paru_install, copy_file

desc = "fastest terminal"


def setup() -> None:
    paru_install(["kitty", "kitty-shell-integration"])

    # copy configuration file
    copy_file("home/.config/kitty/kitty.yml")
