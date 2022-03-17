from src.util import pamac_install, copy_file, smart_mkdir
from src.constants import content_dir
from src.setup.system import polybar

name = "BSPWM (with sxhkd and polybar)"


def setup():
    """window manager"""

    pamac_install(["xorg-xinit", "bspwm", "sxhkd"])
    polybar.setup()

    # copy xinit configuration
    copy_file(f"{content_dir}/home/pomp/.xinitrc", "~/.xinitrc")

    # copy bspwm configuration
    copy_file(
        f"{content_dir}/home/pomp/.config/bspwm/bspwmrc",
        "~/.config/bspwm/bspwmrc",
        # rwxr-xr-x
        755,
    )

    # copy sxhkd configuration
    copy_file(
        f"{content_dir}/home/pomp/.config/sxhkd/sxhkdrc",
        "~/.config/sxhkd/sxhkdrc",
    )
