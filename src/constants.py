from os import environ
from os.path import abspath, dirname

# used to look for resources
# points to repo root
content_dir = abspath(dirname(dirname(__file__)))

# used to temporarily save files
# must be synced with `setup.py`
tmp_dir = "/tmp/com.developomp.setup"

home_dir = environ.get("HOME", "/home/pomp")
