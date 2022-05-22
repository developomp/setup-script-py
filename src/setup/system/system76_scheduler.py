from src.util import paru_install, copy_file


name = "system76 scheduler"


def setup():
    """Process priority optimizer"""

    # using the git version because "system76-scheduler" builds from source too anyway
    paru_install("system76-scheduler-git")
    copy_file(
        "etc/system76-scheduler/assignments/osu.ron",
        sudo=True,
    )
