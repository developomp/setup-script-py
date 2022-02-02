from ..util import pamac_install

name = "Davinci Resolve"


def setup():
    pamac_install("davinci-resolve")
