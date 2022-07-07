from src.util import run, copy_file
from src.constants import tmp_dir

name = "pomky"


def setup():
    """conky but rusty"""

    run(f"git clone --depth 1 https://github.com/developomp/pomky {tmp_dir}/pomky")
    run(f"cd {tmp_dir}/pomky && cargo install --path .")
    copy_file("home/.config/autostart/pomky.desktop")
