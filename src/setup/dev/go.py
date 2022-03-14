from src.util import pamac_install

name = "go"


def setup():
    """Golang stuff"""

    pamac_install("go")
