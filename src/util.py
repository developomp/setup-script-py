from importlib.machinery import SourceFileLoader
from os import system, makedirs, popen
from os.path import dirname
import requests
import zipfile

from src.log import error
import src.constants


def run_and_return(command: str) -> list[str]:
    """Runs command in system shell and return the result.
    This is a blocking function.
    Use this if you want to get the output of the command."""

    return popen(command).readlines()


def paru_install(packages: str | list[str]) -> None:
    """
    Download arch linux packages (including AUR).

    arguments:
        packages: Either a string list of packages or a space-separated list of packages.
    """

    if type(packages) == str:
        pass
    elif type(packages) == list:
        packages = " ".join(packages)
    else:
        error("Invalid paru packages format.")
        return

    system(f"paru -S --noconfirm {packages}")


def flatpak_install(packages: str) -> None:
    """
    Download packages from flathub.

    arguments:
        packages: space-separated list of packages.
    """

    system(f"flatpak install -y {packages}")


def smart_mkdir(path: str) -> None:
    """
    Recursively create directories if it doesn't exist already.
    """

    try:
        makedirs(path)
    except OSError:
        pass


def trash(path) -> None:
    """Moves a file or directory to freedesktop trash."""

    try:
        system(f"trash-put {path}")
    except Exception as err:
        print(f"Failed to remove: {path}")
        raise err


def copy_file(src_file: str, mode="644", sudo=False) -> None:
    """
    Copies a file in the repo to the system.
    If the `src_file` starts with `home/`, it maps to $HOME.
    Otherwise, it maps to `/`.
    This function automatically creates parent directories if they do not exist already.

    parameters:
    - src_file: A path-like object or string pointing to a file.
    - mode: Permission mode (as in chmod). Defaults to 644 (rw-r--r--).
    - sudo: Whether to run command as sudo or not.
    """

    dst_file = str(src_file)

    if dst_file.startswith("home/"):
        dst_file = src.constants.home_dir + dst_file[4:]
    else:
        dst_file = "/" + dst_file

    command = f"install -Dm{mode} {src.constants.content_dir}/{src_file} {dst_file}"

    if sudo:
        command = f"sudo {command}"

    system(command)


def copy_directory(src: str, dst: str) -> None:
    """Copy a directory.
    Automatically creates parent directory/directories of dst if it does not exist already

    parameters:
        src: A path-like object or string pointing to a directory.
        dst: A path-like object or string pointing to a directory.
    """

    system(f"cp -R {src.constants.content_dir}{src} {dst}")


def load_dconf(file_name: str) -> None:
    """Loads dconf configuration"""

    system(f'dconf load / < "{src.constants.content_dir}/files/dconf/{file_name}"')


def download(file_name: str, url: str) -> None:
    """Downloads a file from a url."""
    r = requests.get(url)

    with open(file_name, "wb") as f:
        f.write(r.content)


def unzip(zip_path: str, dst_dir: str) -> None:
    """Unzips a .zip file to a directory."""

    smart_mkdir(dst_dir)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dst_dir)


def import_file(name, path) -> None:
    return SourceFileLoader(name, path).load_module()


def command_exists(command: str) -> bool:
    """Check if a command can be found in the current default shell.
    A copy of this function also exists in `setup.py`."""

    return len(run_and_return(f"command -v {command}")) == 1
