from src.initialize import initialize


def entry():
    initialize()

    # import should happen after the `initialize` function is called
    from src.menu import menu

    menu()
