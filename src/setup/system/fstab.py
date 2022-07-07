from src.util import run

name = "fstab"


def setup():
    """adds /media/pomp/data drive to fstab"""

    fstab_path = "/etc/fstab"

    # check if /media/pomp/data exists already
    with open(fstab_path, "rt") as f:
        if "/media/pomp/data" in f.read():
            return

    line_to_write = (
        "UUID=1cea13a5-ea19-4023-99dd-4bfd062a288c /media/pomp/data ext4 defaults 0 2"
    )

    # append a line to the end and ignore output
    # not using python's file interface because I don't wanna deal with permission stuff
    run(f'echo "{line_to_write}" | sudo tee -a {fstab_path} >/dev/null')
