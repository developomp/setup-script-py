from .initialize import initialize


def entry():
    initialize()

    # import should happen after the `initialize` function is called
    from .interface.choose_action import choose_action

    choose_action()
