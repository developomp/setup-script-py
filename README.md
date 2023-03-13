<h1 align="center">
  My <a href="https://archlinux.org">Arch Linux</a> desktop setup
</h1>

[![what's this?](https://img.shields.io/badge/what's_this%3F-grey?style=for-the-badge)](https://developomp.com/portfolio/linux-setup-script)

## Images

![result image 1](./.github/img/result1.png)

<details>
<summary>Click to see more images</summary>

### Some windows

![result image 2](./.github/img/result2.png)

### Minimalism at its finest

![result image 3](./.github/img/result3.png)

### Script Execution

Main menu:
![Execution 0](./.github/img/execution0.png)

Choosing Action:
![Execution 1](./.github/img/execution1.png)

</details>

## Usage

1. Install base Arch Linux with the following packages
   - `sudo`
   - `networkmanager`
   - `base-devel`
   - `python`
   - `git`
2. Log in as a non-root user with sudo permission
3. Download the setup script
   ```
   curl setup.developomp.com -Lo setup.py
   ```
4. Execute
   ```
   python setup.py
   ```

Full setup could easily take more than a hour depending on the internet speed.

## Overview

### Software

|                 Software | Choice                                                                                     |
| -----------------------: | :----------------------------------------------------------------------------------------- |
| Desktop Environment - 🚀 | [GNOME](https://www.gnome.org)                                                             |
|           GTK theme - 🎨 | [vimix-dark-compact-beryl](https://github.com/vinceliuice/vimix-gtk-themes)                |
|               Shell - 🐚 | [zsh](https://github.com/zsh-users/zsh) with [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) |
|            Terminal - 🖥️ | [alacritty](https://github.com/alacritty/alacritty)                                        |
|        File manager - 📂 | [Nautilus](https://gitlab.gnome.org/GNOME/nautilus)                                        |
|             Browser - 🌐 | [Brave](https://github.com/brave/brave-browser)                                            |
|   Text Editor & IDE - 📝 | [VSCodium](https://github.com/VSCodium/vscodium)                                           |

### Project structure

- `.github/workflows/deploy.yml` - A [github action](https://github.com/features/actions) that makes `setup.py` available at https://setup.developomp.com/
- `etc` - Files that are copied over to the `/etc` directory
- `home` - Files that are copied over to the `/home/pomp` directory
- `files` - Files that are used but does not get copied
  - `dconf` - [dconf](https://wiki.gnome.org/Projects/dconf) files
- `src` - Python scripts. Check code comments (especially `__init__.py`) for more info

## [Hardware](./docs/hardware.md)

## [Game settings](./docs/game-settings.md)

## Sources

### Wallpaper

<img alt="wallpaper" src="./.github/img/wallpaper.png" width="75%">

- [a video](https://www.youtube.com/watch?v=QEWV6fiYaDU) from [Chillhop Music](https://www.youtube.com/channel/UCOxqgCwgOqC2lMqC5PYz_Dg)
- Artwork by [Jeff Östberg](https://jeffostberg.se)
- Animation by [Geneviève Delacroix](http://www.genevievelacroix.com)
- Effects (in order)
  - [nordified](https://github.com/Schrodinger-Hat/ImageGoNord) (filtering option toggled)
  - GIMP gaussian blur 3.5
  - level 1 compression (GIMP)
