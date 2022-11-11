from src.util import appimage_install, get_latest_appimage_url_from_github


name = "Cutter"


def setup():
    """
    Reverse engineering tool with GUI
    """

    appimage_install(
        get_latest_appimage_url_from_github("rizinorg/cutter"),
        "cutter",
    )
