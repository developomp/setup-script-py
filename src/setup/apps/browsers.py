from src.util import flatpak_install, smart_copy
from src.constants import tmp_dir

name = "Browsers"
post_install = ["restore onetab"]


def setup():
    """"""
    # install librewolf
    flatpak_install("io.gitlab.librewolf-community")
    smart_copy(
        f"{tmp_dir}/home/pomp/.config/autostart/librewolf.desktop",
        "~/.config/autostart/librewolf.desktop",
    )
    # todo: settings

    # install ungoogled chromium
    flatpak_install("com.github.Eloston.UngoogledChromium")

    # todo: DNS https cloudflare
    # todo: tor browser
