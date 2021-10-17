export ZSH="/home/pomp/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(
  git
  zsh-interactive-cd
  zsh-syntax-highlighting
)
source $ZSH/oh-my-zsh.sh
export PATH="$PATH:$HOME/.yarn/bin"

export EDITOR=vim
export VISUAL=vim
