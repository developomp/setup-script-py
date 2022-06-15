from src.util import flatpak_install


# Brave handles restoration itself using its own sync stuff
post_install = ["enable sync"]


def setup():
    """The least worst web browser"""

    flatpak_install("com.brave.Browser")
