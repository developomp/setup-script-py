import requests
from pathlib import Path

from src.setup.system import appimagelauncher


name = "Notesnook"


def setup():
    """FOSS video editing utility"""

    download_path = f"{Path.home()}/Applications/notesnook_linux_x86_64.AppImage"
    download_url = (
        "https://notesnook.com/releases/linux/notesnook_linux_x86_64.AppImage"
    )

    appimagelauncher.setup()

    print(f"Downloading AppImage file to {download_path}")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    open(download_path, "wb").write(
        requests.get(download_url, allow_redirects=True).content
    )
