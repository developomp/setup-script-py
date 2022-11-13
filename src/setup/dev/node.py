from src.constants import home_dir
from src.util import paru_install, command_exists
from src.setup.system import zsh
from src.log import log

from os.path import isdir
from os import system

desc = "Javascript everywhere!"


def setup():
    # Install zsh if it's not installed already
    if not command_exists("zsh"):
        zsh.setup()

    paru_install("nvm")

    log("Installing Node.JS LTS")
    system("source /usr/share/nvm/init-nvm.sh; nvm install --lts")

    # todo: add "source /usr/share/nvm/init-nvm.sh" to ~/.zshrc

    log("Installing npm")
    system("npm install --global npm")

    log("Installing pnpm")
    system("npm install --global pnpm")

    log("Installing yarn")
    system("npm install --global yarn")
