import inquirer
from glob import glob
from os.path import exists

from ..util import import_file
from src.log import log
from src.constants import tmp_dir


def choose_action():
    directory_to_search = tmp_dir
    if exists("src/"):
        directory_to_search = "."

    files = glob(f"{directory_to_search}/src/setup/**/*.py")
    files = [
        s.removeprefix(f"{directory_to_search}/src/setup/")
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
        module = import_file(
            action_name, f"{directory_to_search}/src/setup/{action_name}"
        )

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
