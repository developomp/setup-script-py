from src.util import paru_install
from os import system

name = "git"


def setup():
    """What's a branch?"""

    paru_install("git")

    system('git config --global user.email "developomp@gmail.com"')
    system('git config --global user.name "developomp"')
    system("git config --global pull.rebase false")
    system("git config --global init.defaultBranch master")
