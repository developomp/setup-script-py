from src.util import paru_install, copy_file

desc = "Local activity monitor"


def setup():
    paru_install("activitywatch-bin")
    copy_file("home/.config/autostart/activitywatch.desktop")
