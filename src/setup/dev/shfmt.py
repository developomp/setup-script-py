from src.util import pamac_install

name = "shfmt"


def setup():
    """Shell formatter"""

    pamac_install("shfmt")
