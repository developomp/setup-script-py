# must be synced with `setup.py`
# this variable may be altered by the script
# most notably by `src/interface/choose_action.py`

from os import environ

content_dir = "/tmp/com.developomp.setup"
tmp_dir = content_dir
home_dir = environ.get("HOME")
