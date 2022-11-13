from src.util import appimage_install

desc = "FOSS Note taking utility"


def setup():
    appimage_install(
        "https://notesnook.com/releases/linux/notesnook_linux_x86_64.AppImage",
        "notesnook_linux_x86_64",
    )
