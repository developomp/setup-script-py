<h1 align="center">
  My <a href="https://archlinux.org">Arch Linux</a> desktop setup
</h1>

## Purpose

This repository is here to provide myself materials (script, guide, configuration, and other files) for cases when I need to transfer to other machine or reinstall the OS.

## Images

![result image 1](./.repo/result1.png)

<details>
<summary>Click here to see more images</summary>

### Some windows

![result image 2](./.repo/result2.png)

### Minimalism at its finest

![result image 3](./.repo/result3.png)

### Script Execution

![Execution](./.repo/execution.png)

### Selection Menu

![Menu](./.repo/menu.png)

</details>

## Usage

This project is undergoing a rewrite. Use the [old](https://github.com/developomp/setup/tree/old) branch for now.

### WARNING

- The script assumes a clean installation of arch linux. That is, no extra packages installed already.

### Instructions

1. Install arch linux via [archfi](https://github.com/MatMoul/archfi) (included installer via [archinstall](https://github.com/archlinux/archinstall) coming soon).

2. download the setup script

   ```bash
   curl -LO setup.developomp.com
   ```

3. Execute it.

Full setup could easily take more than a hour depending on the internet speed.

## How does it work?

[Github pages](https://pages.github.com) allows the developers to deploy a static website directly from their repositories. I set up github action so that the [`setup.py`](./setup.py) script gets copied to the [`index.html`](https://github.com/developomp/setup/blob/gh-pages/index.html) file in the [`gh-pages`](https://github.com/developomp/setup/tree/gh-pages) branch where it can be accessed from https://setup.developomp.com. The script then downloads necessary files and packages so it can start doing its thing.

## Hardware

<details>
  <summary>Click to see hardware information</summary>

### Laptop

| name    | model                                  |
| ------- | -------------------------------------- |
| Machine | LG 15U480-KP50ML Laptop (15U480-KA5MK) |
| CPU     | intel i5-8250U                         |
| GPU     | Nvidia MX 150                          |

### RAM

| model                             | size |
| --------------------------------- | ---- |
| SK Hynix HMA81GS6AFR8N-UH (stock) | 8GB  |
| Samsung M471A1K43CB1-CRC (added)  | 8GB  |

### Storage

| ID\* | model                                  | Size  |
| ---- | -------------------------------------- | ----- |
| 1    | SK Hynix HFS128G39TND-N210A (30002P10) | 128GB |
| 2    | Samsung SSD 860 PRO 512GB (RVM02B6Q)   | 512GB |

\*arbitrary index I gave. Has no meaning.

### Partitioning

- unallocated space at the end are for overprovisioning
- no swap partition

more information about efi partition can be found in [this](https://wiki.archlinux.org/title/GRUB) arch wiki page.

partitioning done with fdisk ([source](https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git/tree/disk-utils/fdisk.c), [man](https://man7.org/linux/man-pages/man8/fdisk.8.html)).

| drive id\* | format | size                           | mount location   | purpose                           |
| ---------- | ------ | ------------------------------ | ---------------- | --------------------------------- |
| 1          | FAT32  | +300M                          | /boot/efi        | EFI partition                     |
| 1          | ext4   | -15G                           | /                | root                              |
| 2          | ext4   | default (all available sector) | /media/pomp/data | data storage (D drive equivalent) |

\*index from [storage](#Storage)

### Peripherals

|    peripheral | model                                                                                                                                                                                                        |
| ------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         mouse | [Logitech G402 Hyperion fury](https://www.logitechg.com/en-eu/products/gaming-mice/g402-hyperion-fury-fps-gaming-mouse.html) I got from a [giveaway event](https://blog.naver.com/yjcomicsblog/221432692995) |
|     headphone | [NOX NX-2](https://www.e-nox.co.kr/theme/s007/index/product_view01.php?wr_id=16)                                                                                                                             |
| laptop cooler | [ABKO NCORE NC500](http://ncore.co.kr/shop/product_item.php?ItId=2586312930)                                                                                                                                 |

</details>

## Sources

- I randomly change between these wallpapers depending on my mood.
- Some wallpaper images are intentionally blurred to improve transparent overlay readability.

### 3rd Wallpaper

<img alt="3rd wallpaper" src="./.repo/wallpaper3.png" width="75%">

- made by [u/nullcriminal](https://www.reddit.com/r/unixporn/comments/b4dt3y) on reddit

### 2nd Wallpaper

<img alt="2nd wallpaper" src="./.repo/wallpaper2.png" width="75%">

- image from [wallpaperaccess](https://wallpaperaccess.com/full/2752569.png)
- the [image list](https://wallpaperaccess.com/simple-earth) I found it from

### 1st Wallpaper

<img alt="1st wallpaper" src="./.repo/wallpaper1.png" width="75%">

- [a video](https://www.youtube.com/watch?v=QEWV6fiYaDU) from [Chillhop Music](https://www.youtube.com/channel/UCOxqgCwgOqC2lMqC5PYz_Dg)
- Artwork by [Jeff Östberg](https://jeffostberg.se)
- Animation by [Geneviève Delacroix](http://www.genevievelacroix.com)

### System monitor

- [pomky](https://github.com/developomp/pomky) (commit: aecec82)

this [file](./home/pomp/.local/bin/pomky) right here

## Future

<details>
  <summary>Click to show future plans</summary>

### Laptop

#### Features

- Korean keyboard
- Full size arrow keys and number pad
- DP port

maybe:

- ARM / RISC-V CPU
- SoC powered (like apple's M1)

#### Candidates

- [Framework laptop DIY edition](https://frame.work/products/laptop-diy-edition)

Total price: $1098

|               option | my choice                                                                                                  |
| -------------------: | :--------------------------------------------------------------------------------------------------------- |
|          Motherboard | Intel i5-1135G7 (8M Cache, up to 4.20 GHz)                                                                 |
|                 WiFi | Intel® Wi-Fi 6E AX210 No vPro®                                                                             |
|              Storage | 500GB - WD_BLACK™ SN850 NVMe™                                                                              |
|     Operating system | None                                                                                                       |
|               Memory | 16GB (2 x 8GB) DDR4-3200                                                                                   |
|             Keyboard | **waiting** for Korean keyboard w/ full size arrow key and number pad                                      |
|              Display | **waiting** for 120+Hz display                                                                             |
|        Power Adapter | **waiting** for [Schuko plug (type f plug)](https://www.worldstandards.eu/electricity/plugs-and-sockets/f) |
| Port expansion cards | 1xDP 3xUSB-A 2xUSB-C 1xHDMI + **waiting** for RJ-45 ethernet port                                          |

### Storage

1TB HDD for long-term backup

### Mouse

#### Features

- consistent tracking
- 1000Hz+ polling rate

#### Candidates

- [Logitech G pro wireless](https://www.logitechg.com/en-us/products/gaming-mice/pro-wireless-mouse)
- [logitech G pro X](https://www.logitechg.com/en-us/products/gaming-mice/pro-x-superlight-wireless-mouse)

with:

- [Logitech powerplay](https://www.logitechg.com/en-us/products/gaming-mouse-pads/powerplay-wireless-charging)

### Monitor

#### Features

- Refresh rate: 165Hz
- resolution: 1920x1080 (FHD)

#### Candidates

- [Newsync X250FG ZERO](http://prod.danawa.com/info/?pcode=9295200)

### Keyboard

#### Features

- programmable
- pantograph
- number pad
- full size arrow keys

#### Candidates

None

</details>
