from src.util import flatpak_install

name = "GNOME extension manager"


def setup():
    """GNOME extension manager without using browsers"""

    flatpak_install("com.mattjakeman.ExtensionManager")
