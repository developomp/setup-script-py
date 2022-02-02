from .initialize import initialize
from .ui.show_main_menu import show_main_menu


def entry():
    initialize()
    show_main_menu()
