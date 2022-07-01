import inquirer


class Choices:
    RUN_SETUP_SCRIPTS = "Run setup scripts"
    INSTALL_ARCH_LINUX = "Install Arch Linux"
    QUIT = "Quit"


def menu():
    """Show menu screen."""

    print("\n")

    questions = [
        inquirer.List(
            "menu",
            message="What would you like to do?",
            choices=[
                Choices.RUN_SETUP_SCRIPTS,
                Choices.INSTALL_ARCH_LINUX,
                Choices.QUIT,
            ],
        ),
    ]

    choice = inquirer.prompt(questions)["menu"]

    if choice == Choices.RUN_SETUP_SCRIPTS:
        from src.interface.choose_action import choose_action

        choose_action()
        input("\nSetup complete! (press Enter to return to menu)")
        menu()
    elif choice == Choices.INSTALL_ARCH_LINUX:
        input("Work In Progress (press Enter to return to menu)")
        menu()
    elif choice == Choices.QUIT:
        # return to `setup.py` so it can exit safely
        return
    else:
        print(
            """You should not have been able to reach this side of the code,
yet here you are. Consider this an easter egg."""
        )
        exit(1)
