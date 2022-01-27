import os


def initialize():
    """
    - install [pytermgui](https://github.com/bczsalba/pytermgui)
    - install pip
    - install flatpak
    """

    #
    # Install flatpak
    #

    os.system("sudo pacman -S --noconfirm --needed flatpak")
