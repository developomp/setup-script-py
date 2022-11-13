from os import system

desc = "adds /home/pomp to fstab"


def setup():
    fstab_path = "/etc/fstab"

    # check if /home/pomp exists already
    with open(fstab_path, "rt") as f:
        if "/home/pomp" in f.read():
            return

    line_to_write = "UUID=1cea13a5-ea19-4023-99dd-4bfd062a288c /home/pomp auto 0 0"

    # append a line to the end and ignore output
    # not using python's file interface because I don't wanna deal with permission stuff
    system(f'echo "{line_to_write}" | sudo tee -a {fstab_path} >/dev/null')
