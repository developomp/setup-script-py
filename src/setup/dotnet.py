from ..util import pamac_install

name = ".NET"


def setup():
    """Microsoft java"""

    pamac_install("dotnet-sdk")
