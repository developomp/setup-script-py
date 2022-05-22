from src.util import paru_install, copy_file, remove_directory
from src.constants import content_dir, home_dir
from src import log

from os.path import isdir
from os import system

name = "Zsh"


def setup():
    """Objectively better shell"""

    paru_install("zsh")

    log.log("Installing Oh My Zsh")
    system(
        'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
    )

    log.log("Installing powerlevel10k theme")
    p10k_path = f"{home_dir}/.oh-my-zsh/custom/themes/powerlevel10k"
    remove_directory(p10k_path)
    system(
        f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git {p10k_path}"
    )

    log.log("Installing zsh syntax highlighter")
    zsh_syntax_highlighting_path = (
        f"{home_dir}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
    )
    remove_directory(zsh_syntax_highlighting_path)
    system(
        f"git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git {zsh_syntax_highlighting_path}"
    )

    # apply zshrc configuration
    copy_file("home/.zshrc")

    # set the default terminal to zsh
    system("chsh -s /bin/zsh")
