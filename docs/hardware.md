# hardware

## Desktop

No desktop

## Laptop

|    name | model                                                                                                          |
| ------: | :------------------------------------------------------------------------------------------------------------- |
| Machine | [LG 15U480-KP50ML](https://www.lge.co.kr/kr/business/product/common/redirectProductDetail.do?prdId=MD00040678) |
|     CPU | intel i5-8250U                                                                                                 |
|     GPU | Nvidia MX 150                                                                                                  |

## RAM

|                             model | capacity |
| --------------------------------: | :------- |
| SK Hynix HMA81GS6AFR8N-UH (stock) | 8GB      |
|  Samsung M471A1K43CB1-CRC (added) | 8GB      |

## Storage

- Model: [Samsung 860 PRO SSD 512GB](https://www.samsung.com/sec/support/model/MZ-76P512BW/)
- total size: 512,110,190,592 bytes (476.9 GiB, 512.1 GB)

Partitions (in order):

| format | size (parenthesis = rounded values)         | mount location   | purpose           |
| ------ | ------------------------------------------- | ---------------- | ----------------- |
| ext4   | 432,109,780,992 bytes (402.4 GiB, 432.1 GB) | /media/pomp/data | data storage      |
| FAT32  | 524,288,000 bytes (500.0 MiB, 524.3 MB)     | /boot            | EFI partition     |
| ext4   | 64,424,509,440 bytes (60.0 GiB, 64.4 GB)    | /                | system root       |
| N/A    | 15,050,546,688 bytes (14.0 GiB, 15.0 GB)    | N/A              | over-provisioning |

## Peripherals

|     peripheral | model                                                                                                                                                                                                        |
| -------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|          mouse | [Logitech G402 Hyperion fury](https://www.logitechg.com/en-eu/products/gaming-mice/g402-hyperion-fury-fps-gaming-mouse.html) I got from a [giveaway event](https://blog.naver.com/yjcomicsblog/221432692995) |
|      headphone | [NOX NX-2](https://www.e-nox.co.kr/theme/s007/index/product_view01.php?wr_id=16)                                                                                                                             |
|  laptop cooler | [ABKO NCORE NC500](http://ncore.co.kr/shop/product_item.php?ItId=2586312930)                                                                                                                                 |
|       Keyboard | YMDK wings                                                                                                                                                                                                   |
| Drawing tablet | secondhand [wacom CTL-472 (one by wacom)](https://www.wacom.com/en-us/products/pen-tablets/one-by-wacom) (using since May 8, 2022)                                                                           |
|        Monitor | secondhand [HP X24ih](https://www.hp.com/us-en/shop/pdp/hp-x24ih-gaming-monitor) ([review](https://www.rtings.com/monitor/reviews/hp/x24ih)) (using since May 21, 2022)                                      |

### Keyboard

- Parts & Accessories:
  - [Case + PCB + Stabilizers + Cable](https://ko.aliexpress.com/item/1005003330613995.html) (white)
  - [walnut wrist rest](https://ko.aliexpress.com/item/1005003629440348.html)
  - [foam](https://ko.aliexpress.com/item/1005004451001013.html) (PCB & Bottom Foam)
  - [Switches](https://www.aliexpress.com/item/1005003891937604.html) (Outemu silent peach)
  - [Switch Opener](https://www.coupang.com/vp/products/6176660507?vendorItemId=79812876139)
  - [Switch Film](https://www.aliexpress.com/item/1005002885279946.html) (HTV+PC 0.18mm)
  - [Lube](https://www.aliexpress.com/item/1005002297786498.html) (GPL205 G0 7.6g)
  - [Keycaps](https://www.aliexpress.com/item/1005003834670594.html) (Korean subs)
- Mods:
  - [holee mod](https://www.youtube.com/watch?v=-vhpHjlkRgQ)
  - band-aided stabilizer bottom
- QMK config:
  - Layer 0
    ![layer 0](../.repo/kbd_layer_0.png)
  - Layer 1
    ![layer 1](../.repo/kbd_layer_1.png)

How to compile and flash the firmware on Linux:

- install qmk cli
- run qmk setup: `qmk setup -y`
- copy the [`keyboard`](../files/keyboard/) directory to `~/qmk_firmware/keyboards/ymdk/wingshs/keymaps` and rename it to `pomp`
- flash the board: `qmk flash --clean --keyboard ymdk/wingshs --keymap pomp`
  - unplug board
  - plug it back while holding <kbd>Space</kbd>+<kbd>B</kbd>. Keep holding it for a second
