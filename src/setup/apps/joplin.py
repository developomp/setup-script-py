from src.util import flatpak_install

name = "Joplin"
post_install = ["Sync with oneDrive"]


def setup():
    """FOSS note-taking app"""

    flatpak_install("net.cozic.joplin_desktop")
