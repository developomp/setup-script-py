from src.util import flatpak_install, copy_file
from os import system


desc = "vscode without spyware"


EXTENSIONS = (
    "aaron-bond.better-comments",
    "bierner.jsdoc-markdown-highlighting",
    "dbaeumer.vscode-eslint",
    "denoland.vscode-deno",
    "DigitalBrainstem.javascript-ejs-support",
    "dsznajder.es7-react-js-snippets",
    "eamodio.gitlens",
    "earshinov.sort-lines-by-selection",
    "EditorConfig.EditorConfig",
    "esbenp.prettier-vscode",
    "foxundermoon.shell-format",
    "geequlim.godot-tools",
    "golang.go",
    "jeff-tian.markdown-katex",
    "jock.svg",
    "matklad.rust-analyzer",
    "mhutchie.git-graph",
    "ms-python.python",
    "ms-toolsai.jupyter",
    "ms-toolsai.jupyter-keymap",
    "ms-toolsai.jupyter-renderers",
    "ms-vscode.hexeditor",
    "naumovs.color-highlight",
    "nico-castell.linux-desktop-file",
    "PKief.material-icon-theme",
    "qwtel.sqlite-viewer",
    "Razoric.gdscript-toolkit-formatter",
    "redwan-hossain.auto-rename-tag-clone",
    "serayuzgur.crates",
    "streetsidesoftware.code-spell-checker",
    "styled-components.vscode-styled-components",
    "svelte.svelte-vscode",
    "tamasfe.even-better-toml",
    "XadillaX.viml",
    "zhuangtongfa.material-theme",
)


def setup():
    flatpak_install("com.vscodium.codium")

    # codium --list-extensions
    for extension in EXTENSIONS:
        system(f"codium --install-extension {extension} --force")

    # vscodium settings
    copy_file("home/.var/app/com.vscodium.codium/config/VSCodium/User/settings.json")

    # enable vscode extension store
    copy_file("home/.var/app/com.vscodium.codium/config/VSCodium/product.json")
