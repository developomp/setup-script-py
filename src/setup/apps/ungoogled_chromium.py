from src.util import flatpak_install
from src.constants import content_dir, home_dir

name = "Ungoogled chromium"
post_install = ["restore onetab"]


def setup():
    """A web browser"""

    flatpak_install("com.github.Eloston.UngoogledChromium")

    config_path = f"{home_dir}/.var/app/com.github.Eloston.UngoogledChromium/config/chromium/System Profile"
