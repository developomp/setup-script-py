from src.util import paru_install, load_dconf

name = "Nautilus"


def setup():
    """File viewer for GNOME"""

    paru_install(
        [
            "nautilus",
            "nautilus-open-any-terminal",  # allow nautilus to use alacrittty terminal
        ]
    )

    load_dconf("nautilus.conf")
