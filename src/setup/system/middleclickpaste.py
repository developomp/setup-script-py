from src.util import paru_install

desc = "Prevents middle click paste"
post_install = ["restart"]


def setup():
    paru_install("xmousepasteblock-git")
