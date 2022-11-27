from src.util import paru_install
from src.log import log
from os import system

desc = "Javascript everywhere!"


def setup():
    paru_install(["nodejs-lts-hydrogen", "npm"])

    log("Installing npm")
    system("npm install --global npm")

    log("Installing pnpm")
    system("npm install --global pnpm")

    log("Installing yarn")
    system("npm install --global yarn")
