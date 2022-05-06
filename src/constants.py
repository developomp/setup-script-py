# must be synced with `setup.py`
# this variable may be altered by the script
# most notably by `src/interface/choose_action.py`

from os import system

content_dir = "/tmp/com.developomp.setup"
tmp_dir = content_dir
home_dir = "/home/pomp"
is_zsh_available: bool = system("command -v zsh &> /dev/null") == 0
