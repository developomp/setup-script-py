from src.util import paru_install

desc = "System backup and restoration utility"


def setup():
    paru_install("timeshift")
