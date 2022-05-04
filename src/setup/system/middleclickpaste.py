from src.util import paru_install

name = "middle click paste"
post_install = ["restart"]


def setup():
    """Prevents middle click paste"""

    paru_install("xmousepasteblock-git")
