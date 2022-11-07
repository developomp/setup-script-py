from src.util import paru_install, load_dconf
from src import log

from os import system

name = "GNOME extensions"
post_install = ["Restart GNOME shell", "enable GNOME extensions"]


EXTENSIONS = (
    (36, "extension-lockkeys.conf"),  # lock-keys
    (906, "extension-sound-output-device-chooser.conf"),  # sound-output-device-chooser
    (2741, ""),  # remove-alttab-delay-v2
    (2890, "extension-trayIconsReloaded.conf"),  # tray-icons-reloaded
    (3193, "extension-blur-my-shell.conf"),  # blur-my-shell
    (4000, "extension-barbar.conf"),  # babar
    (4158, ""),  # gnome-40-ui-improvements
)


def setup():
    """
    Extensions for the GNOME Desktop environment

    Intentionally left out chrome-gnome-shell because I won't be using browsers to install GNOME extensions.

        gnome-shell-extension-installer: gnome extension installer CLI
        gnome-shell-extension-pop-shell-git: window tiling extension
    """

    paru_install(
        [
            "gnome-shell-extension-installer",
            # not using gnome-shell-extension-pop-shell because it builds from source too anyway
            # not using gnome-shell-extension-pop-shell-bin because GNOME version isn't compatible
            "gnome-shell-extension-pop-shell-git",
        ]
    )

    load_dconf("extension-pop-shell.conf")

    for (extension, dconf_file) in EXTENSIONS:
        log.log("installing: https://extensions.gnome.org/extension/$1")
        system(f"gnome-shell-extension-installer {extension} --yes --update")

        if dconf_file:  # if dconf_file is not empty
            load_dconf(dconf_file)
