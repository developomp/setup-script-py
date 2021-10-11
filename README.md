<p align="center">
  My <a href="https://archlinux.org">Arch linux</a> desktop setup
</p>

---

[![LICENSE: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)

## Purpose

To provide myself materials (script, guide, and other files) for cases when I need to transfer to other machine or reinstall the OS.

Result:<br />
![result image](./result.png)

## Instructions

> **WARNING:** This script is written for my laptop ONLY.

1. Install arch linux via [archfi](https://github.com/MatMoul/archfi).

   - latest arch linux version as of writing: `2021.10.01`

2. Create user `pomp`

   ```bash
   useradd -m pomp # create user and home directory
   EDITOR=vim visudo # edit sudoers file with vim
   # enable wheel group
   usermod -aG wheel pomp # give pomp sudo access
   ```

3. Execute the [`setup.sh`](./setup.sh) script.
4. Profit.

Full setup could easily take more than a hour depending on the internet speed.

Execution:<br />
![Execution](./execution.png)

Selection Menu:<br />
![Menu](./menu.png)

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

### Wallpaper 1

<img alt="wallpaper 1. Cozy cafe with large window" src="./wallpaper1.png" width="75%">

- [a video](https://www.youtube.com/watch?v=QEWV6fiYaDU) from [Chillhop Music](https://www.youtube.com/channel/UCOxqgCwgOqC2lMqC5PYz_Dg)
- Artwork by [Jeff Östberg](https://jeffostberg.se​)
- Animation by [Geneviève Delacroix](http://www.genevievelacroix.com)

### Wallpaper 2

<img alt="wallpaper 2. An astronaut on moon looking at earth" src="./wallpaper2.png" width="75%">

- image from [wallpaperaccess](https://wallpaperaccess.com/full/2752569.png)
- the [image list](https://wallpaperaccess.com/simple-earth) I found it from

## Future

1TB hard drive for backup + redundancy
