from src.util import copy_file, command_exists
from src.constants import tmp_dir

desc = "conky but rusty"


def setup():
    if not command_exists("pomky"):
        system(
            f"git clone --depth 1 https://github.com/developomp/pomky {tmp_dir}/pomky"
        )
        system(f"cd {tmp_dir}/pomky && cargo install --path .")

    copy_file("home/.config/autostart/pomky.desktop")
