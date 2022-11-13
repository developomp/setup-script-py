from src.util import paru_install
from os import system

desc = "The thing everyone pretends they know how it works"


def setup():
    paru_install("git")

    system('git config --global user.email "developomp@gmail.com"')
    system('git config --global user.name "developomp"')
    system("git config --global pull.rebase false")
    system("git config --global init.defaultBranch master")
    system("git config --global credential.helper store")
