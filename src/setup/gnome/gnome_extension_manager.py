from src.util import flatpak_install

desc = "GNOME extension manager without using browsers"


def setup():
    flatpak_install("com.mattjakeman.ExtensionManager")
