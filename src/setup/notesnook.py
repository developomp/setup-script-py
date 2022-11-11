from src.util import appimage_install

name = "Notesnook"


def setup():
    """FOSS Note taking utility"""

    appimage_install(
        "https://notesnook.com/releases/linux/notesnook_linux_x86_64.AppImage",
        "notesnook_linux_x86_64",
    )
