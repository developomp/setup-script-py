from .. import deno, dotnet, go, jdk, rust, vscodiumm

name = "dev"


def setup():
    """development related stuff"""

    deno.setup()
    dotnet.setup()
    go.setup()
    jdk.setup()
    rust.setup()
    vscodium.setup()
