<h1 align="center">
  My <a href="https://archlinux.org">Arch Linux</a> desktop setup
</h1>

## Purpose

This repo is here to provide myself materials (script, guide, config files, and other files) for cases when I need to transfer to other machine or reinstall the OS.

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

- This script is written to work in my hardware **EXCLUSIVELY**.
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

[Github pages](https://pages.github.com) allows the developers to deploy a static website using a branch of their repositories to store the static files. I set up github action so that the [`setup.py`](./setup.py) script gets copied to the `index.html` file in the [`gh-pages`](https://github.com/developomp/setup/tree/gh-pages) branch where it is deployed to https://setup.developomp.com. The script then downloads necessary files and packages when necessary.

## Hardware

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

## Sources

I randomly change between these wallpapers depending on my mood.

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

https://github.com/developomp/pomky

this [file](./home/pomp/.local/bin/pomky) right here

commit: aecec82

## Future

- 1TB HDD for long-term backup
- [wannabuy](https://developomp.com/wannabuy)
