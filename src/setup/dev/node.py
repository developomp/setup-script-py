from src.constants import home_dir
from src.util import paru_install, run, command_exists
from src.setup.system import zsh
from src import log

from os.path import isdir

name = "node"


def setup():
    """
    Javascript outside of browsers!

    https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally

     nvm: NodejS version manager
    pnpm: better node package manager
    yarn: better node package manager
    """

    # Install zsh if it's not installed already
    if not command_exists("zsh"):
        zsh.setup()

    paru_install("nvm")

    log.log("Installing Node.JS LTS")
    run("source /usr/share/nvm/init-nvm.sh; nvm install --lts")

    # todo: add "source /usr/share/nvm/init-nvm.sh" to ~/.zshrc

    log.log("Installing npm")
    run("npm install --global npm")

    log.log("Installing pnpm")
    run("npm install --global pnpm")

    log.log("Installing yarn")
    run("npm install --global yarn")
