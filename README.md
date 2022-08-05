<h1 align="center">
  My <a href="https://archlinux.org">Arch Linux</a> desktop setup
</h1>

[![what's this?](https://img.shields.io/badge/what's_this%3F-grey?style=for-the-badge)](https://developomp.com/portfolio/linux-setup-script)

## Table of contents

<details>
<summary>Click to show table of contents</summary>

- [Table of contents](#table-of-contents)
- [Images](#images)
  - [Some windows](#some-windows)
  - [Minimalism at its finest](#minimalism-at-its-finest)
  - [Script Execution](#script-execution)
- [How does it work?](#how-does-it-work)
- [Usage](#usage)
- [Hardware](#hardware)
  - [Laptop](#laptop)
  - [RAM](#ram)
  - [Storage](#storage)
  - [Partitioning](#partitioning)
  - [Peripherals](#peripherals)
- [Sources](#sources)
  - [3rd Wallpaper](#3rd-wallpaper)
  - [2nd Wallpaper](#2nd-wallpaper)
  - [1st Wallpaper](#1st-wallpaper)
  - [System monitor](#system-monitor)
- [Future plans](#future-plans)
  - [Laptop](#laptop-1)
  - [Storage](#storage-1)
  - [Mouse](#mouse)
  - [Monitor](#monitor)

</details>

## Images

![result image 1](./.repo/result1.png)

<details>
<summary>Click here to see more images</summary>

### Some windows

![result image 2](./.repo/result2.png)

### Minimalism at its finest

![result image 3](./.repo/result3.png)

### Script Execution

Main menu:
![Execution 0](./.repo/execution0.png)

Choosing Action:
![Execution 1](./.repo/execution1.png)

</details>

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
- `.repo` - Extraneous files that does not serve any functional purpose
- `etc` - Files that are copied over to the `/etc` directory
- `home` - Files that are copied over to the `/home/pomp` directory
- `files` - Files that are used but does not get copied
  - `dconf` - [dconf](https://wiki.gnome.org/Projects/dconf) files
- `src` - Python scripts. Check code comments (especially `__init__.py`) for more info

## Usage

1. Install Arch linux.

   A built-in installer (using [archinstall](https://github.com/archlinux/archinstall)) will be added in the future.
   In the meantime, use [archfi](https://github.com/MatMoul/archfi) instead.
   [`sudo`](https://archlinux.org/packages/core/x86_64/sudo/) and [`wget`](https://archlinux.org/packages/extra/x86_64/wget/), and [`paru-bin`](https://aur.archlinux.org/packages/paru-bin/) must be installed.

2. Create a user.

   Create a user in wheel group and create a home directory:

   ```bash
   useradd -G wheel -m pomp
   ```

   Allow user to use sudo:

   ```bash
   EDITOR=vim visudo
   ```

   Now, log in to the user account.

3. Download the setup script.

   ```bash
   wget setup.developomp.com -O setup.py
   ```

4. Execute it.

   ```bash
   python ./setup.py
   ```

Full setup could easily take more than a hour depending on the internet speed.

## Hardware

<details>
  <summary>Click to see hardware information</summary>

### Desktop

No desktop

### Laptop

| name    | model                                                                                                          |
| ------- | -------------------------------------------------------------------------------------------------------------- |
| Machine | [LG 15U480-KP50ML](https://www.lge.co.kr/kr/business/product/common/redirectProductDetail.do?prdId=MD00040678) |
| CPU     | intel i5-8250U                                                                                                 |
| GPU     | Nvidia MX 150                                                                                                  |

### RAM

| model                             | size |
| --------------------------------- | ---- |
| SK Hynix HMA81GS6AFR8N-UH (stock) | 8GB  |
| Samsung M471A1K43CB1-CRC (added)  | 8GB  |

### Storage

- Model: [Samsung 860 PRO SSD 512GB](https://www.samsung.com/sec/support/model/MZ-76P512BW/)
- total size: 512,110,190,592 bytes (476.9 GiB, 512.1 GB)

Partitions sorted by order:

| format | size (parenthesis = rounded values)         | mount location   | purpose           |
| ------ | ------------------------------------------- | ---------------- | ----------------- |
| ext4   | 432,109,780,992 bytes (402.4 GiB, 432.1 GB) | /media/pomp/data | data storage      |
| FAT32  | 524,288,000 bytes (500.0 MiB, 524.3 MB)     | /boot            | EFI partition     |
| ext4   | 64,424,509,440 bytes (60.0 GiB, 64.4 GB)    | /                | system root       |
| N/A    | 15,050,546,688 bytes (14.0 GiB, 15.0 GB)    | N/A              | over-provisioning |

### Peripherals

|     peripheral | model                                                                                                                                                                                                        |
| -------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|          mouse | [Logitech G402 Hyperion fury](https://www.logitechg.com/en-eu/products/gaming-mice/g402-hyperion-fury-fps-gaming-mouse.html) I got from a [giveaway event](https://blog.naver.com/yjcomicsblog/221432692995) |
|      headphone | [NOX NX-2](https://www.e-nox.co.kr/theme/s007/index/product_view01.php?wr_id=16)                                                                                                                             |
|  laptop cooler | [ABKO NCORE NC500](http://ncore.co.kr/shop/product_item.php?ItId=2586312930)                                                                                                                                 |
|       Keyboard | YMDK wings                                                                                                                                                                                                   |
| Drawing tablet | secondhand [wacom CTL-472 (one by wacom)](https://www.wacom.com/en-us/products/pen-tablets/one-by-wacom) (using since May 8, 2022)                                                                           |
|        Monitor | secondhand [HP X24ih](https://www.hp.com/us-en/shop/pdp/hp-x24ih-gaming-monitor) ([review](https://www.rtings.com/monitor/reviews/hp/x24ih)) (using since May 21, 2022)                                      |

#### Keyboard

<!-- <p align="center">
  <b>Video</b>
  <a href="https://youtu.be/8vBm4MfOPME"><img alt="Keyboard sound test" src="https://img.youtube.com/vi/8vBm4MfOPME/maxresdefault.jpg" /></a>
</p> -->

- Parts & Accessories:
  - [Case + PCB + Stabilizers + Cable](https://ko.aliexpress.com/item/1005003330613995.html) (white)
  - [walnut wrist rest](https://ko.aliexpress.com/item/1005003629440348.html)
  - [foam](https://ko.aliexpress.com/item/1005004451001013.html) (PCB & Bottom Foam)
  - [Switches](https://www.aliexpress.com/item/1005003891937604.html) (Outemu silent peach)
  - [Switch Opener](https://www.coupang.com/vp/products/6176660507?vendorItemId=79812876139)
  - [Switch Film](https://www.aliexpress.com/item/1005002885279946.html) (HTV+PC 0.18mm)
  - [Lube](https://www.aliexpress.com/item/1005002297786498.html) (GPL205 G0 7.6g)
  - [Keycaps](https://www.aliexpress.com/item/1005001500813840.html) (Korean subs)
- Mods:
  - [holee mod](https://www.youtube.com/watch?v=-vhpHjlkRgQ)
  - band-aided stabilizer bottom
- QMK config:
  - Layer 0
    ![layer 0](.repo/kbd_layer_0.png)
  - Layer 1
    ![layer 1](.repo/kbd_layer_1.png)

How to compile and flash the firmware on Linux:

- install qmk cli
- run qmk setup: `qmk setup -y`
- copy the [`keyboard`](./files/keyboard/) directory to `~/qmk_firmware/keyboards/ymdk/wingshs/keymaps` and rename it to `pomp`
- flash the board: `qmk flash --clean --keyboard ymdk/wingshs --keymap pomp`
  - unplug board
  - plug it back while holding <kbd>Space</kbd>+<kbd>B</kbd>. Keep holding it for a second

</details>

## Sources

<details>
  <summary>Click to show asset source</summary>

### Wallpaper

<img alt="wallpaper" src="./.repo/wallpaper.png" width="75%">

- [a video](https://www.youtube.com/watch?v=QEWV6fiYaDU) from [Chillhop Music](https://www.youtube.com/channel/UCOxqgCwgOqC2lMqC5PYz_Dg)
- Artwork by [Jeff Östberg](https://jeffostberg.se)
- Animation by [Geneviève Delacroix](http://www.genevievelacroix.com)
- Effects (in order)
  - [nordified](https://github.com/Schrodinger-Hat/ImageGoNord) (filtering option toggled)
  - GIMP gaussian blur 3.5
  - level 1 compression (GIMP)

</details>

## Future plans

<details>
  <summary>Click to show future plans</summary>

### Laptop

- Features:
  - price: less than 1 million KRW
  - display:
    sie: 15in
    resolution: 1920x1080 pixels (FHD)
    frame rate: 144Hz
    panel type: IPS
  - keyboard:
    - legends: Korean
    - arrow keys: full size, ㅗ shaped
  - CPU:
    - performance: better than intel i5-8250U
    - ISA: x86_64 (or ARM architecture if becomes mainstream)
  - GPU:
    - performance: better than Nvidia MX-150
    - non-hybrid, single GPU (preferably internal)
  - RAM:
    - gen: DDR5
    - size: 16G
  - SSD:
    - interface: M.2
    - protocol: NVMe
    - capacity: 512 GB
  - OS: None (will install Arch Linux)
- Candidates:
  - None

### Storage

- 1TB HDD for long-term backup

### Mouse

- Features:
  - go forward / backward button
  - wireless
  - click latency: faster than Logitech G402 without wires
  - weight: lighter than Logitech G402
  - size: similar to Logitech G402
  - max polling rate: no lower, and no higher than 1000Hz
- Candidates:
  - Razer Viper Ultimate ([rtings review](https://www.rtings.com/mouse/reviews/razer/viper-ultimate), [techpowerup review](https://www.techpowerup.com/review/razer-viper-ultimate/))

### Monitor

- Features:
  - panel: not decided / does not exist
    - no burn-in
    - fast response time (at least faster than my [current monitor](#peripherals))
    - individual pixel lighting (for true black)
    - color accurate
  - normal RGB stripe subpixel layout
  - refresh rate: 144+ Hz
  - size: at most 24in
  - resolution: FHD (1920x1080)
  - flicker-free
- Candidates:
  - None

</details>
