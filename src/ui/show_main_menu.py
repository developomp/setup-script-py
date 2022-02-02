from argparse import ArgumentParser, Namespace
from subprocess import run

import pytermgui as ptg


def show_main_menu():
    with ptg.WindowManager() as manager:
        window = ptg.Window(
            ptg.Label("[wm-title]menu"),
            ptg.Label(),
            ptg.Button("Exit!", lambda *_: manager.exit()),
        )

        manager.add(window)
        manager.run()
