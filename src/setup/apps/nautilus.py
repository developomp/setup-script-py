from src.util import paru_install, load_dconf, command_exists, run
from src.setup.apps import terminal


name = "Nautilus"


def setup():
    """File viewer for GNOME"""

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
    run(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal kitty"
    )
    run(
        "gsettings set com.github.stunkymonkey.nautilus-open-any-terminal keybindings ''"
    )
    run("gsettings set com.github.stunkymonkey.nautilus-open-any-terminal new-tab true")
