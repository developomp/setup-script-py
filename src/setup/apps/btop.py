from ...util import pamac_install

name = "Btop"


def setup():
    """top but better"""

    pamac_install("btop")
