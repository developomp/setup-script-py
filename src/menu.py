import inquirer
from glob import glob
from os.path import exists, abspath

from src.util import import_file
from src.log import log
from src.constants import content_dir


def choose_action():
    files = glob(f"{content_dir}/src/setup/**/*.py")
    files = [
        s.removeprefix(f"{content_dir}/src/setup/")
        for s in files
        if "__init__.py" not in s
    ]

    response = inquirer.prompt(
        [
            inquirer.Checkbox(
                "actions",
                message="What do you want to set up?",
                choices=files,
            ),
        ]
    )

    post_install_tasks = []
    for action_name in response["actions"]:
        module = import_file(action_name, f"{content_dir}/src/setup/{action_name}")

        if hasattr(module, "post_install"):
            if isinstance(module.post_install, str):
                post_install_tasks.append(module.post_install)
            else:
                post_install_tasks += module.post_install

        log(f"Setting up: {module.name} ({action_name})")
        module.setup()

    if post_install_tasks:
        print("POST INStALL TASKS:")
        for post_install_task in post_install_tasks:
            print(f"- {post_install_task}")


def menu():
    """Show menu screen."""

    print("\n")
    choose_action()
    input("\nSetup complete! (press Enter to return to menu)")
    menu()
