from src.util import paru_install, copy_file
from os import system


desc = "vscode without spyware"


# codium --list-extensions
EXTENSIONS = (
    "aaron-bond.better-comments",
    "ahmadalli.vscode-nginx-conf",
    "alexcvzz.vscode-sqlite",
    "astro-build.astro-vscode",
    "bierner.jsdoc-markdown-highlighting",
    "bierner.markdown-mermaid",
    "bpruitt-goddard.mermaid-markdown-syntax-highlighting",
    "bradlc.vscode-tailwindcss",
    "coolbear.systemd-unit-file",
    "damildrizzy.fastapi-snippets",
    "dbaeumer.vscode-eslint",
    "dbankier.vscode-quick-select",
    "denoland.vscode-deno",
    "DigitalBrainstem.javascript-ejs-support",
    "dsznajder.es7-react-js-snippets",
    "eamodio.gitlens",
    "earshinov.sort-lines-by-selection",
    "EditorConfig.EditorConfig",
    "esbenp.prettier-vscode",
    "eww-yuck.yuck",
    "formulahendry.auto-rename-tag",
    "foxundermoon.shell-format",
    "geequlim.godot-tools",
    "golang.go",
    "GraphQL.vscode-graphql",
    "GraphQL.vscode-graphql-syntax",
    "icsharpcode.ilspy-vscode",
    "jeff-tian.markdown-katex",
    "jock.svg",
    "mhutchie.git-graph",
    "mikestead.dotenv",
    "ms-azuretools.vscode-docker",
    "ms-dotnettools.csharp",
    "ms-dotnettools.vscode-dotnet-runtime",
    "ms-python.isort",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "ms-toolsai.jupyter-keymap",
    "ms-toolsai.jupyter-renderers",
    "ms-toolsai.vscode-jupyter-cell-tags",
    "ms-toolsai.vscode-jupyter-slideshow",
    "ms-vscode.cpptools",
    "ms-vscode.hexeditor",
    "ms-vscode.mono-debug",
    "naumovs.color-highlight",
    "neikeq.godot-csharp-vscode",
    "nico-castell.linux-desktop-file",
    "PKief.material-icon-theme",
    "qwtel.sqlite-viewer",
    "Razoric.gdscript-toolkit-formatter",
    "rust-lang.rust-analyzer",
    "serayuzgur.crates",
    "stkb.rewrap",
    "streetsidesoftware.code-spell-checker",
    "styled-components.vscode-styled-components",
    "svelte.svelte-vscode",
    "tamasfe.even-better-toml",
    "Terrastruct.d2",
    "tintinweb.vscode-decompiler",
    "unifiedjs.vscode-mdx",
    "vivaxy.vscode-conventional-commits",
    "XadillaX.viml",
    "yzhang.markdown-all-in-one",
    "zhuangtongfa.material-theme",
)


def setup():
    # not using flatpak version due to permission issues
    # such as lazydocker not working
    paru_install("vscodium-bin")

    for extension in EXTENSIONS:
        system(f"codium --install-extension {extension} --force")

    # vscodium settings
    copy_file("home/.config/VSCodium/User/settings.json")

    # enable vscode extension store
    copy_file("home/.config/VSCodium/product.json")
