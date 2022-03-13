import inquirer
from glob import glob


def choose_action():
    files = glob("src/setup/**/*.py")
    files = [s.removeprefix("src/setup/") for s in files if "__init__.py" not in s]

    response = inquirer.prompt(
        [
            inquirer.Checkbox(
                "actions",
                message="What do you want to set up?",
                choices=files,
            ),
        ]
    )

    print(response["actions"])
