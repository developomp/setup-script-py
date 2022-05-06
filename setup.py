#!/usr/bin/env python3

"""
developomp's arch linux setup script

This file is all that's needed for execution.
It'll download all the dependencies and related files automatically.
"""

from os import system, geteuid, popen
from os.path import exists
from shutil import rmtree
import sys

# must be synced with `src/constants.py`
tmp_dir = "/tmp/com.developomp.setup"

#
# Util
#
# These commands are from `src/util.py`.
# Comments can only be found over there.
#


def silent_system(command: str) -> None:
    system(f"{command} &> /dev/null")


def command_exits(command: str) -> bool:
    return len(popen(f"command -v {command}").readlines()) == 1


#
# Common
#


def cleanup():
    """Removes temporary files and folders downloaded by this script"""

    if exists(tmp_dir):
        rmtree(tmp_dir)


#
# Checks
#


def exit_if_root():
    """Exits script if it was executed as root"""

    # todo: allow running script as root when implementing user creation/arch installation logic
    if geteuid() == 0:
        print("Do not run this script as root.", file=sys.stderr)
        exit(1)


def exit_if_invalid_python_version():
    """Exits script if python version is lower than 3.7"""

    # todo: implement

    pass


def exit_if_system_not_compatible():
    """Exits script if the OS is not linux or if pacman does not exist"""

    print("Checking if system is compatible")
    if "linux" not in sys.platform.lower() or not command_exits("pacman"):
        print("This script should only be used on arch linux.", file=sys.stderr)
        exit(1)


def exit_if_no_internet():
    """Exits script if there's no internet connection.
    Pings archlinux.org for testing."""

    print("Checking if there's internet connection")
    if silent_system("ping -c 1 archlinux.org"):
        print("Failed to connect to internet.", file=sys.stderr)
        exit(1)


#
# Initializations
#


def install_git():
    """Installs git if it's not installed already"""

    print("Initializing git")
    if not command_exits("git"):
        print("git was not installed already. Installing now.")
        system("sudo pacman -S --noconfirm --needed git")


def clone_repository():
    """Clone this repository (https://github.com/developomp/setup) to `/tmp` directory"""

    print("Cloning git repository")

    # remove existing files first
    cleanup()

    # clone repository
    if silent_system(
        f"git clone --depth 1 https://github.com/developomp/setup.git {tmp_dir}"
    ):
        print("Failed to clone repository", file=sys.stderr)
        exit(1)

    # allow everyone to read and write.
    if system(f"chmod -R a+rw {tmp_dir}"):
        print("Failed to change file permission for cloned repo", file=sys.stderr)
        exit(1)


#
#
#


def minimal_check():
    """
    Minimal checks before executing any code.
    Full checks will happen after downloading codes from the internet
    """

    exit_if_root()
    exit_if_invalid_python_version()
    exit_if_system_not_compatible()
    exit_if_no_internet()


def minimal_initialization():
    """
    Does minimal initialization.
    Full initialization will happen after downloading codes from the internet.
    """

    install_git()

    # skip if testing
    if exists(".git/") and exists("src/"):
        return

    clone_repository()

    # Add cloned directory to system path
    sys.path.append(tmp_dir)


#
#
#


def main():
    minimal_check()
    minimal_initialization()

    from src.entry import entry

    entry()

    cleanup()


if __name__ == "__main__":
    main()
