from src.util import paru_install, run

name = "git"


def setup():
    """What's a branch?"""

    paru_install("git")

    run('git config --global user.email "developomp@gmail.com"')
    run('git config --global user.name "developomp"')
    run("git config --global pull.rebase false")
    run("git config --global init.defaultBranch master")
    run("git config --global credential.helper store")
