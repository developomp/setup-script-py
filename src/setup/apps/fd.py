from src.util import pamac_install

name = "fd"


def setup():
    """find but modern and rusty"""

    pamac_install("fd")
