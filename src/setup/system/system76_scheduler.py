from src.util import paru_install, copy_file
from src.constants import content_dir

name = "system76 scheduler"


def setup():
    """Process priority optimizer"""

    # using the git version because "system76-scheduler" builds from source too anyway
    paru_install("system76-scheduler-git")
    copy_file(
        f"{content_dir}/etc/system76-scheduler/assignments/osu.ron",
        "/etc/system76-scheduler/assignments/osu.ron",
        sudo=True,
    )
