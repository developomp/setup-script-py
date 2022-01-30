from ..util import pamac_install

name = "deno"


def setup():
    """
    nodejs++

    check .zshrc for bin path stuff
    """

    pamac_install("deno")
