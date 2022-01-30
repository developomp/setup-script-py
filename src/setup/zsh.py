from ..util import pamac_install, smart_copy
from ..constants import tmp_dir
from .. import log

from os.path import isdir
from os import system

name = "Zsh"


def setup():
    """Objectively better shell"""

    pamac_install("zsh")

    if not isdir("/home/pomp/.oh-my-zsh"):
        log.log("zsh already configured. Skipping.")
        return

    # install oh my zsh
    system(
        'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
    )

    # install powerlevel10k theme
    system(
        "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
    )

    # install syntax highlighter
    system(
        "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
    )

    # apply zshrc configuration
    smart_copy(f"{tmp_dir}/home/pomp/.zshrc", "~/.zshrc")
