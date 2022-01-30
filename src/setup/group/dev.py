from .. import deno, dotnet, rust, vscodiumm

name = "dev"


def setup():
    """development related stuff"""

    deno.setup()
    dotnet.setup()
    rust.setup()
    vscodium.setup()
