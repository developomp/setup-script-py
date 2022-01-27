#!/usr/bin/env python3

"""
developomp's arch linux setup script

This file is all that's needed for execution.
It'll download all the dependencies and related files automatically.
"""

import os
import sys
from shutil import rmtree


def minimal_check():
    """
    Minimal checks before executing any code.
    Full checks will happen after downloading codes from the internet
    """

    # check if the script is running as root
    # todo: allow running script as root when implementing user creation/arch installation logic
    if os.geteuid() == 0:
        print("Do not run this script as root.", file=sys.stderr)
        exit(1)

    # todo: check if python version is higher than 3.7

    # check if OS is linux and if pacman exists
    print("Checking if system is compatible")
    if "linux" not in sys.platform.lower() or os.system(
        "command -v pacman &> /dev/null"
    ):
        print("This script should only be used on arch linux.", file=sys.stderr)
        exit(1)

    # ping archlinux.org to test if there's internet connection
    print("Checking if there's internet connection")
    if os.system("ping -c 1 archlinux.org &> /dev/null"):
        print("Failed to connect to internet.", file=sys.stderr)
        exit(1)


def minimal_initialization():
    """
    Does minimal initialization.
    Full initialization will happen after downloading codes from the internet.
    """

    print("Initializing git")
    if os.system("command -v git &> /dev/null"):
        print("git was not installed already. Installing now.")
        os.system("sudo pacman -S --noconfirm --needed git")

    #
    # Download necessary files
    #

    print("Cloning git repository")

    tmp_dir = "/tmp/com.developomp.setup"

    # remove existing files
    if os.path.exists(tmp_dir):
        rmtree(tmp_dir)

    # todo: change branch to master when merging with master
    if os.system(
        f"git clone --depth 1 -b dev https://github.com/developomp/setup.git {tmp_dir} &> /dev/null"
    ):
        print("Failed to clone repository", file=sys.stderr)
        exit(1)

    # allow everyone to read and write but not execute.
    if os.system(f"chmod -R a+rw {tmp_dir}"):
        print("Failed to change file permission for cloned repo", file=sys.stderr)
        exit(1)

    #
    # Add cloned directory to path
    #

    sys.path.append(tmp_dir)


def main():
    minimal_check()
    minimal_initialization()

    from src.entry import entry

    # hand over control to cloned code
    entry()


if __name__ == "__main__":
    main()
