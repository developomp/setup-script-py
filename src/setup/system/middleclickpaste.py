from ...util import pamac_install

name = "middle click paste"
post_install = ["restart"]


def setup():
    """Prevents middle click paste"""

    pamac_install("xmousepasteblock-git")
