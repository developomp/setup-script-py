from src.util import paru_install, smart_mkdir, download, unzip
from src.constants import tmp_dir, home_dir
from shutil import rmtree, move
from os import remove, system
from os.path import exists, basename
import requests
import glob

name = "fonts"

# path to temporarily save font related files
TMP_FONTS_DIRECTORY = f"{tmp_dir}/tmp/fonts"

# fonts to download
FONT_NAMES = (
    "Audiowide",
    "Varela Round",
    "Noto Sans Mono",
    "Nanum Gothic Coding",
    "Noto Emoji",
)

# where to unzip the fonts
FONT_INSTALL_DIR = f"{home_dir}/.local/share/fonts"


def setup():
    """
    System fonts

    adobe-source-han-sans-kr-fonts: Korean font
                       ttf-baekmuk: Korean font
                     unicode-emoji: Colorful emojis
                  ttf-iosevka-nerd: Terminal font
    """

    paru_install(
        [
            "adobe-source-han-sans-kr-fonts",
            "ttf-baekmuk",
            "unicode-emoji",
            "ttf-iosevka-nerd",
        ]
    )

    smart_mkdir(TMP_FONTS_DIRECTORY)

    # download and unzip font files if they're not downloaded already
    for font_name in FONT_NAMES:
        zip_path = f"{TMP_FONTS_DIRECTORY}/{font_name}.zip"

        # download and unzip if either zip file or unzipped directory exists
        download(zip_path, f"https://fonts.google.com/download?family={font_name}")
        unzip(zip_path, f"{TMP_FONTS_DIRECTORY}/{font_name}")
        remove(zip_path)

    smart_mkdir(FONT_INSTALL_DIR)

    # "install" fonts
    for ttf_file_path in glob.glob(f"{TMP_FONTS_DIRECTORY}/**/*.ttf"):
        move(ttf_file_path, f"{FONT_INSTALL_DIR}/{basename(ttf_file_path)}")

    # regenerate font cache
    system("fc-cache -vf")

    # cleanup
    rmtree(TMP_FONTS_DIRECTORY)
