from os import system
from src.util import silent_system, copy_file
from src.constants import tmp_dir

name = "pomky"


def setup():
    """conky but rusty"""

    silent_system(
        f"git clone --depth 1 https://github.com/developomp/pomky {tmp_dir}/pomky"
    )
    silent_system(f"cd {tmp_dir}/pomky && cargo install --path .")
    copy_file("home/.config/autostart/pomky.desktop")
