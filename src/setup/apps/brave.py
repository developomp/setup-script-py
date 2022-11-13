from src.util import flatpak_install

desc = "The least worst web browser"

# Brave handles restoration itself using its own sync stuff
post_install = ["enable sync"]


def setup():
    flatpak_install("com.brave.Browser")
