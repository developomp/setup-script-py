from src.util import paru_install, load_dconf, command_exists
from src.setup.apps import alacritty
from os import system

name = "Nautilus"


def setup():
    """File viewer for GNOME"""

    paru_install(
        [
            "nautilus",
            "nautilus-open-any-terminal",  # allow nautilus to use alacrittty terminal
        ]
    )

    if not command_exists("alacritty"):
        alacritty.setup()

    # set nautilus settings
    load_dconf("nautilus.conf")

    # set nautilus terminal settings
    system(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal alacritty"
    )
    system(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal keybindings ''"
    )
    system(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal new-tab true"
    )
