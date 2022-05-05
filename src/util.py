from .constants import content_dir
from .log import error

from importlib.machinery import SourceFileLoader
from os import system, makedirs
from os.path import dirname
import requests
import zipfile


def paru_install(packages: str | list[str]) -> None:
    """
    Download arch linux packages (including AUR).

    arguments:
        packages: Either a string list of packages or a space-separated list of packages.
    """

    if type(packages) == str:
        system(f"paru -S --noconfirm {packages}")
    elif type(packages) == list:
        packages = " ".join(packages)
        system(f"paru -S --noconfirm {packages}")
    else:
        error("Invalid paru packages format.")


def flatpak_install(packages: str) -> None:
    """
    Download packages from flathub.

    arguments:
        packages: space-separated list of packages.
    """

    system(f"flatpak install -y {packages}")


def smart_mkdir(path: str):
    """
    Recursively create directories if it doesn't exist already.
    """

    try:
        makedirs(path)
    except OSError:
        pass


def remove_directory(path):
    try:
        system(f"rm -rf {path}")
    except Exception as err:
        print(f"Failed to remove directory: {path}")
        raise err


def copy_file(src: str, dst: str, mode="644"):
    """
    Copies src to dst.
    Automatically creates parent directory/directories of dst if it does not exist already.

    parameters:
        src: A path-like object or string pointing to a file.
        dst: A path-like object or string pointing to a file.
        mode: Permission mode (as in chmod). Defaults to 644 (rw-r--r--)
    """

    system(f"install -Dm{mode} {src} {dst}")


def copy_directory(src: str, dst: str):
    """Copy a directory.
    Automatically creates parent directory/directories of dst if it does not exist already

    parameters:
        src: A path-like object or string pointing to a directory.
        dst: A path-like object or string pointing to a directory.
    """

    system(f"cp -R {src} {dst}")


def load_dconf(file_name: str):
    """Loads dconf configuration"""

    system(f'dconf load / < "{content_dir}/dconf/{file_name}"')


def download(file_name: str, url: str):
    """Downloads a file from a url."""
    r = requests.get(url)

    with open(file_name, "wb") as f:
        f.write(r.content)


def unzip(zip_path: str, dst_dir: str):
    """Unzips a .zip file to a directory."""

    smart_mkdir(dst_dir)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dst_dir)


def import_file(name, path):
    return SourceFileLoader(name, path).load_module()


"""
def setup_essentials():
    setup_fstab
    sudo pacman -S --needed base-devel wget
    dconf

    # install dialog if it's not installed already
    if ! command -v dialog &>/dev/null; then
        log "dialog was not installed already. Installing now..."
        package_install dialog
    fi

def backup():
	TIMESTAMP=$(date +%s)
	# backup dconf configuration
	dconf dump / >"$SCRIPT_DIR/dconf$TIMESTAMP.conf"

	# make a home directory backup
	rsync -a --info=progress2 --perms /home/pomp "$DATA_PATH/backup$TIMESTAMP"

	# create timeshift backup
	if ! command -v timeshift &>/dev/null; then
		error "failed to create timeshift backup. Timeshift command not found."
	else
		sudo timeshift --create --comments "auto created by developomp setup script ($TIMESTAMP)"
	fi
"""
