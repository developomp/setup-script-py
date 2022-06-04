<h1 align="center">
  My <a href="https://archlinux.org">Arch Linux</a> desktop setup
</h1>

[![what's this?](https://img.shields.io/badge/what's_this%3F-grey?style=for-the-badge)](https://developomp.com/portfolio/linux-setup-script)

<p align="center">
  <b>
    This project is undergoing a rewrite. Use the <a href="https://github.com/developomp/setup/tree/old">old branch</a> for now.
  </b>
</p>

## Table of contents

<details>
<summary>Click to expand</summary>

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

![Execution](./.repo/execution.png)

</details>

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

|     peripheral | model                                                                                                                                                                                                        |
| -------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|          mouse | [Logitech G402 Hyperion fury](https://www.logitechg.com/en-eu/products/gaming-mice/g402-hyperion-fury-fps-gaming-mouse.html) I got from a [giveaway event](https://blog.naver.com/yjcomicsblog/221432692995) |
|      headphone | [NOX NX-2](https://www.e-nox.co.kr/theme/s007/index/product_view01.php?wr_id=16)                                                                                                                             |
|  laptop cooler | [ABKO NCORE NC500](http://ncore.co.kr/shop/product_item.php?ItId=2586312930)                                                                                                                                 |
|       Keyboard | [COX CK01 PBT SL](https://www.abko.co.kr/brand/detail.php?it_id=1630976200)                                                                                                                                  |
| Drawing tablet | secondhand [wacom CTL-472 (one by wacom)](https://www.wacom.com/en-us/products/pen-tablets/one-by-wacom)                                                                                                     |
|        Monitor | secondhand [HP X24ih](https://www.hp.com/us-en/shop/pdp/hp-x24ih-gaming-monitor) ([review](https://www.rtings.com/monitor/reviews/hp/x24ih))                                                                 |

#### Keyboard

- Lubed with Krytox 103
- With a towel underneath
- With [COX COS1 walnut wrist rest](https://www.abko.co.kr/brand/detail.php?it_id=1609120628)

<p align="center">
  <b>Video</b>
  <a href="https://youtu.be/8vBm4MfOPME"><img alt="Keyboard sound test" src="https://img.youtube.com/vi/8vBm4MfOPME/maxresdefault.jpg" /></a>
</p>

</details>

## Sources

<details>
  <summary>Click to show asset source</summary>

- I randomly change between these wallpapers depending on my mood.
- Some wallpaper images are intentionally blurred to improve transparent overlay readability.

### 3rd Wallpaper

<img alt="3rd wallpaper" src="./.repo/wallpaper3.png" width="75%">

- made by [u/nullcriminal](https://www.reddit.com/r/unixporn/comments/b4dt3y)

### 2nd Wallpaper

<img alt="2nd wallpaper" src="./.repo/wallpaper2.png" width="75%">

- image from [wallpaperaccess](https://wallpaperaccess.com/full/2752569.png)
- the [image list](https://wallpaperaccess.com/simple-earth) I found it from
- Effects
  - lv1 compression (GIMP)
  - blur (GIMP gaussian blur 3.0)
  - [nordified](https://github.com/Schrodinger-Hat/ImageGoNord) (filtering option toggled)

### 1st Wallpaper

<img alt="1st wallpaper" src="./.repo/wallpaper1.png" width="75%">

- [a video](https://www.youtube.com/watch?v=QEWV6fiYaDU) from [Chillhop Music](https://www.youtube.com/channel/UCOxqgCwgOqC2lMqC5PYz_Dg)
- Artwork by [Jeff Östberg](https://jeffostberg.se)
- Animation by [Geneviève Delacroix](http://www.genevievelacroix.com)
- Effects
  - lv1 compression (GIMP)
  - blur (GIMP gaussian blur 3.5)
  - [nordified](https://github.com/Schrodinger-Hat/ImageGoNord) (filtering option toggled)

### System monitor

- [pomky](https://github.com/developomp/pomky) (commit: 8fce169)

[this file](./home/pomp/.local/bin/pomky) right here

</details>

## Future plans

<details>
  <summary>Click to show future plans</summary>

### Laptop

- Features:
  - less than 1 million KRW (around 780 USD)
  - Korean keyboard
  - FHD monitor
  - number pad
  - x86_64 architecture
  - NO NVIDIA GPU
- Candidates:
  - [Samsung NT750XDZ-A51A](http://prod.danawa.com/info/?pcode=14186387)

### Storage

- 1TB HDD for long-term backup

### Mouse

- Features:
  - <=7ms wired click latency
  - <=80g weight
  - Either from Razer or Logitech
- Candidates:
  - [Razer Viper 8k](https://www.rtings.com/mouse/reviews/razer/viper-8khz/)
  - [Razer Viper Mini](https://www.rtings.com/mouse/reviews/razer/viper-mini/)
  - [Razer Viper Ultimate](https://www.rtings.com/mouse/reviews/razer/viper-ultimate/)
- Notes:
  - Replace piper with [openrazer](https://github.com/openrazer/openrazer) if switching to Razer mouse

### Keyboard

- Planned mods for current keyboard:
  - fix stabilizer rattle (holee mod)
  - lube some under-lubed keys (under-lubed due to not enough lube)
  - sound dampener
- Candidates:
  - [MODE Sonnet](https://modedesigns.com/products/sonnet) (V0G1D2E3A4B5A6A7A8A9A)
    - option (Base $299, $369 with options, $58.33 shipping):
      - Top: White (+$15)
      - Bottom: Gold (+$10)
      - Accent: Gold
      - Internal Weight: Black
      - Plate:
        - Layout: Universal
        - Variant: Aluminum
      - PCB: Hot-swap (+$10)
      - Silicon Base: Black (+$15)
      - Plate foam: Yes (+$10)
      - Feet: Black
      - Plate Caps: Black
    - additional parts and accessories:
      - stabilizers: [Durock V2](https://modedesigns.com/products/durock-v2-stabilizers) ($17)
      - switch (linear, silent, milky?): not decided
      - keycap: [matcha green tea](https://kprepublic.com/products/matcha-green-tea-dye-sub-keycap-set-thick-pbt-for-keyboard-gh60-poker-87-tkl-104-ansi-xd64-bm60-xd68-xd84-xd96-janpanese) (normal Korean variant)
      - wrist rest: not decided
      - switch lube: not decided
      - stabilizer stem lube (dielectric grease): not decided
    - mods:
      - holee mod
      - silicon dampener (optional)
      - memory foam filling
      - un-warp PBT keycaps with hot water
      - no:
        - tempest tape mod

### Monitor

- Features:
  - panel: burn-in-less OLED (ex: QD-OLED)
  - refresh rate: 144+ Hz
  - size: at most 24in
  - resolution: FHD (1920x1080)
- Candidates:
  - None

</details>
