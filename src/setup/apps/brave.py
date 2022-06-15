from src.util import flatpak_install


def setup():
    """The least worst web browser"""

    flatpak_install("com.brave.Browser")
