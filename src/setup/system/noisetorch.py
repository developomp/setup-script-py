from src.util import paru_install, run, copy_file

name = "NoiseTorch"


def setup():
    """AI-powered microphone noise reduction"""

    # temporarily using noisetorch-git over noisetorch-bin due to this:
    # https://github.com/noisetorch/NoiseTorch/issues/274
    paru_install("noisetorch-git")

    # Start NoiseTorch on boot
    # https://github.com/noisetorch/NoiseTorch/wiki/Start-automatically-with-Systemd

    copy_file("home/.config/systemd/user/noisetorch.service")
    run("systemctl --user daemon-reload")
    run("systemctl --user start  noisetorch")
    run("systemctl --user enable noisetorch")
