from src.util import pamac_install
from os import system

name = "node"


def setup():
    """
    Javascript outside of browsers!

    https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally

    nodejs: Javascript on servers!
       nvm: NodejS version manager
       npm: node package manager
      yarn: better node package manager

    check .zshrc for bin path stuff
    """

    pamac_install(["nodejs", "nvm", "npm", "yarn"])
