from src.initialize import initialize


def entry():
    initialize()

    # import should happen after the `initialize` function is called
    from src.interface.menu import menu

    menu()
