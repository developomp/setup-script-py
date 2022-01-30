from .. import deno, dotnet, vscodium

name = "dev"


def setup():
    """development related stuff"""

    deno.setup()
    dotnet.setup()
    vscodium.setup()
