from src.util import flatpak_install, copy_file
from src.constants import content_dir

name = "Ungoogled chromium"
post_install = ["restore onetab"]


def setup():
    """A web browser"""

    flatpak_install("com.github.Eloston.UngoogledChromium")

    # todo: user profile
    # todo: extensions (install and configure)
    # todo: unlock google extension store

    config_path = "/home/pomp/.var/app/com.github.Eloston.UngoogledChromium/config/chromium/System Profile"
