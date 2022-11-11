from src.util import paru_install

name = "Calendar"


def setup():
    """GNOME calendar"""

    # not using the flatpak version because it doesn't integrate well with the GNOME shell
    paru_install("gnome-calendar")
