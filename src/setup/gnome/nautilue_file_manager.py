from src.util import paru_install, load_dconf, command_exists
from src.setup.dev import kitty
from os import system

desc = "GNOME file manager"


def setup():
    paru_install(
        [
            "nautilus",
            "nautilus-open-any-terminal",  # allow nautilus to use kitty terminal
        ]
    )

    if not command_exists("kitty"):
        terminal.setup()

    # set nautilus settings
    load_dconf("nautilus.conf")

    # set nautilus terminal settings
    system(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal kitty"
    )
    system(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal keybindings ''"
    )
    system(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal new-tab true"
    )
