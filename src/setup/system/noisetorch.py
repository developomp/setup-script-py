from src.util import paru_install

name = "NoiseTorch"


def setup():
    """AI-powered microphone noise reduction"""

    # temporarily using noisetorch-git over noisetorch-bin due to this:
    # https://github.com/noisetorch/NoiseTorch/issues/274
    paru_install("noisetorch-git")
