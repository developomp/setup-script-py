from os import system, makedirs
from shutil import copy
from .constants import tmp_dir

# todo: remove all uses of AUR (use pacman instead of pamac)
def pamac_install(packages: str | list[str]) -> None:
    """
        Download package from the arch repository and AUR.

    arguments:
        packages: space-separated list of packages.
    """

    if type(packages) == str:
        system(f"pamac install --no-confirm {packages}")
    elif type(packages) == list[str]:
        packages = packages.join(" ")
        system(f"pamac install --no-confirm {packages}")


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


def smart_copy(src: str, dst: str):
    """
    Copies src to dst.
    Errors if parent directory/directories of dst does not exist.

    arguments:
        src: A path-like object or string pointing to a file.
        dst: A path-like object or string pointing to a file or a directory.
    """

    copy(src, dst)


def load_dconf(file_name: str):
    """Loads dconf configuration"""

    system(f'dconf load / < "{tmp_dir}/dconf/{file_name}"')


"""
def setup_essentials():
    setup_fstab
    sudo pacman -S --needed base-devel wget
    dconf

    # install pamac if it does not exist
    if ! command -v pamac &>/dev/null; then
        log "pamac was not installed already. Installing now..."
        setup_pamac
    fi

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
