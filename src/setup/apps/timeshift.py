from src.util import pamac_install

name = "timshift"


def setup():
    """System backup and restoring utility"""

    pamac_install("timeshift")
