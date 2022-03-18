from src.util import pamac_install
from os import system

name = "Intel CPU undervolting"


def setup():
    """
    Haha efficiency go brrrrt
    https://wiki.archlinux.org/index.php/Undervolting_CPU
    """

    pamac_install("intel-undervolt")

    #
    # configuration
    #

    config_file_path = "/etc/intel-undervolt.conf"

    # create backup
    system(f"sudo install --backup {config_file_path} {config_file_path}.bak")

    # Explanation:
    #   for lines that are not comments (lines that do not start with "#")
    #          search for: "undervolt <number> '<field>' <original value><comment>"
    #   and replaces with: "undervolt <number> '<field>' -100 <comment>"
    #
    # WARNING:
    #   This method does not preserve the space between the value and the comment.
    #   So this:
    #     value  # space between comment and value: 2
    #   becomes this:
    #     value # space between comment and value: 1
    system(
        f"sudo sed -i -e \"/^[^#]/s/\(undervolt [0-9]* 'CPU'\) .*\(#.*\)/\1 -100 \2/\" {config_file_path}"
    )
    system(
        f"sudo sed -i -e \"/^[^#]/s/\(undervolt [0-9]* 'CPU Cache'\) .*\(#.*\)/\1 -100 \2/\" {config_file_path}"
    )

    # apply config changes
    system("sudo intel-undervolt apply")

    # enable undervolting
    system("sudo systemctl enable intel-undervolt")
