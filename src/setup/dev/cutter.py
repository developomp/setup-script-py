from src.util import appimage_install, get_latest_appimage_url_from_github

desc = "Reverse engineering tool with GUI"


def setup():
    appimage_install(
        get_latest_appimage_url_from_github("rizinorg/cutter"),
        "cutter",
    )
