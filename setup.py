#!/usr/bin/env python3

"""
> developomp's Arch Linux setup script <

For more information, please refer to the repository (https://github.com/developomp/setup).
"""

from os import system, geteuid, popen
from os.path import exists
from shutil import rmtree
import sys

# must be synced with `src/constants.py`
tmp_dir = "/tmp/com.developomp.setup"

#
# Utility functions
#
# These functions are copied from `src/util.py`.
# Comments can only be found over there.
#


def silent_system(command: str, suppress_error: bool = True) -> None:
    if suppress_error:
        system(f"{command} &> /dev/null")
    else:
        system(f"{command} > /dev/null")


def run(command: str) -> list[str]:
    return popen(command).readlines()


def command_exists(command: str) -> bool:
    return len(run(f"command -v {command}")) == 1


#
# Check functions
#
# Checks environment incompatibility and apply fix if possible.
#


def minimal_check():
    """
    Minimal checks before executing any code.
    Full checks will happen after downloading codes from the internet
    """

    print("Running checks...")

    exit_if_root()
    exit_if_invalid_python_version()
    exit_if_os_not_compatible()
    exit_if_no_internet()


def exit_if_root():
    """Terminate execution if the script is being executed with superuser privilege."""

    if geteuid() == 0:
        print("  Do not run this script as root.", file=sys.stderr)
        exit(1)


def exit_if_invalid_python_version():
    """Terminates execution if the python version is lower than 3.7"""

    if sys.version_info.major != 3 or sys.version_info.minor < 7:
        from platform import python_version

        print(
            f"  Your python version ({python_version()}) does not meet the minimum requirement (3.7).",
            file=sys.stderr,
        )
        exit(1)


def exit_if_os_not_compatible():
    """Terminate execution if the OS is not Arch Linux based."""

    if "linux" not in sys.platform.lower() or not command_exists("pacman"):
        print("  Incompatible OS.", file=sys.stderr)
        exit(1)


def exit_if_no_internet():
    """Exits script if there's no internet connection.
    Pings archlinux.org for testing."""

    if silent_system("ping -c 1 archlinux.org"):
        print("  Failed to connect to the internet.", file=sys.stderr)
        exit(1)


#
# Bootstrap functions
#


def bootstrap():
    """
    Does minimal initialization.
    Full initialization will happen after downloading codes from the internet.
    """

    print("Bootstrapping...")

    install_git()

    # When testing, there is no need to download the repository.
    if not exists("src/"):
        clone_repository()

        # Add cloned directory to system path
        sys.path.append(tmp_dir)

    from src.entry import entry

    entry()


def install_git():
    """Install git if it's not installed already."""

    if not command_exists("git"):
        system("sudo pacman -S --noconfirm --needed git")


def clone_repository():
    """Clone the setup repository (https://github.com/developomp/setup) to `/tmp` directory"""

    # remove existing files first
    cleanup()

    # clone repository
    if silent_system(
        f"git clone --depth 1 https://github.com/developomp/setup.git {tmp_dir}"
    ):
        print("  Failed to clone repository", file=sys.stderr)
        exit(1)

    # allow everyone to read and write.
    if system(f"chmod -R a+rw {tmp_dir}"):
        print("  Failed to change file permission for cloned repo", file=sys.stderr)
        exit(1)


#
# Main function
#


def main():
    minimal_check()
    bootstrap()

    # Cleanup
    # Remove temporary files downloaded by this script
    if exists(tmp_dir):
        rmtree(tmp_dir)


if __name__ == "__main__":
    main()
