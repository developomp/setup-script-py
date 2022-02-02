"""
setup scripts require two things: name and setup function.
name is a string that contains what it'll show in the list, and setup() is what'll run when it is selected.

name: string
post_install: array or string
setup: function
"""

from . import *


"""
setup_cpu_undervolting() {
	# intel CPU undervolting for less heat and power consumption
	# https://wiki.archlinux.org/index.php/Undervolting_CPU

	package_install intel-undervolt

	config_file=/etc/intel-undervolt.conf

	# create backup in case anything goes wrong
	sudo install --backup $config_file $config_file.bak

	# Explanation:
	#   for lines that are not comments (lines that do not start with a hash)
	#   search for        "undervolt <number> '<field>' <original value><comment>"
	#   and replaces with "undervolt <number> '<field>' -100 <comment>"
	# This method does not preserve the space between the value and the comment.
	# So this:
	#   value  # space between comment and value: 2
	# becomes this:
	#   value # space between comment and value: 1
	sudo sed -i -e "/^[^#]/s/\(undervolt [0-9]* 'CPU'\) .*\(#.*\)/\1 -100 \2/" $config_file
	sudo sed -i -e "/^[^#]/s/\(undervolt [0-9]* 'CPU Cache'\) .*\(#.*\)/\1 -100 \2/" $config_file

	sudo intel-undervolt apply
	sudo systemctl enable intel-undervolt
}

setup_docker() {
	package_install docker

	sudo usermod -aG docker "${USER}"
	sudo systemctl --now enable docker
}

setup_filezilla() {
	package_install filezilla
}

setup_fstab() {
	if cat /etc/fstab | grep "/media/pomp/data" &>/dev/null; then
		return
	fi

	echo "UUID=1cea13a5-ea19-4023-99dd-4bfd062a288c /media/pomp/data ext4 defaults 0 2" | sudo tee -a /etc/fstab >/dev/null
	log "added /media/pomp/data to fstab"
}

setup_dns() {
	:
	# https://1.1.1.1
}

setup_git() {
	package_install git

	git config --global user.email "developomp@gmail.com"
	git config --global user.name "developomp"
	git config --global pull.rebase false
	git config --global init.defaultBranch master
}

setup_gnome() {
	# gnome, nvidia driver, and optimus manager

	# gdm-prime             gdm patched for optimus laptops
	# vimix-cursors         cursors
	# vimix-gtk-themes-git  gtk theme
	# papirus-icon-theme    icon theme
	# gnome-backgrounds     wallpapers and shit
	# gwe                   nvidia GPU overclocking https://gitlab.com/leinardi/gwe
	# nvidia                nvidia GPU support
	# nvidia-settings       nvidia settings
	# lib32-nvidia-utils    32bit nvidia driver utils
	# optimus-manager-qt    https://github.com/Shatur/optimus-manager-qt

	package_install \
		gdm-prime \
		vimix-cursors \
		vimix-gtk-themes-git \
		papirus-icon-theme \
		gnome-backgrounds \
		gwe \
		nvidia \
		nvidia-settings \
		lib32-nvidia-utils \
		optimus-manager-qt

	sudo systemctl enable gdm
	sudo systemctl enable optimus-manager

	install ./home/pomp/.config/autostart/gwe.desktop ~/.config/autostart/
	install ./home/pomp/.config/autostart/io.optimus_manager.OptimusManagerQt.desktop ~/.config/autostart/

	# prevent rootless X
	sudo install -g root -o root -m u=rw,g=r,o=r ./etc/X11/Xwrapper.config /etc/X11/Xwrapper.config
	load_dconf "gnome-desktop-interface.conf"

	# set nvidia preferred mode on login
	install ./home/pomp/.nvidia-preferred-mode.sh ~/
	install ./home/pomp/.config/autostart/nvidia-preferred-mode.desktop ~/.config/autostart/

	setup_gnome_apps
	setup_alacritty # so I have a terminal to work with when only gnome is installed

	cat >~/.config/user-dirs.dirs <<EOL
XDG_DESKTOP_DIR="$HOME/Desktop"
XDG_DOWNLOAD_DIR="/media/pomp/data/Downloads"
XDG_TEMPLATES_DIR="$HOME/Templates"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_DOCUMENTS_DIR="/media/pomp/data/Documents"
XDG_MUSIC_DIR="/media/pomp/data/Music"
XDG_PICTURES_DIR="/media/pomp/data/Pictures"
XDG_VIDEOS_DIR="/media/pomp/data/Videos"
EOL

	# Not using power switching
	# read this wiki[^1] about power management with acpi call for more information
	# [^1]: https://github.com/Askannz/optimus-manager/wiki/A-guide--to-power-management-options#configuration-4--acpi_call

	# todo: gwe mode: ultra(270,660)

	POST_INSTALL+=("gnome: reboot")
}

setup_gnome_apps() {

	# alacarte:                    application menu editor
	# baobab:                      Disk usage analysis
	# cheese:                      take photo/video with camera
	# dconf-editor:                GUI for dconf
	# eog:                         photo viewer
	# evince:                      document viewer
	# file-roller:                 compress & decompress files/directories
	# gnome-calculator:            scientific calculator
	# gnome-characters:            Search for emojis, special characters, and symbols
	# gnome-clocks:                For multiple clocks for different time zones
	# gnome-control-center:        gnome settings
	# gnome-disk-utility:          gnome disk management
	# gnome-font-viewer:           Managing fonts
	# gnome-keyring:               passwords and keys
	# gnome-logs:                  GUI for systemd journal
	# gnome-screenshot:            take screenshots
	# gnome-system-monitor:        show system processes
	# gnome-tweaks:                shows extra settings
	# gpick:                       color picker
	# nautilus:                    gnome file manager
	# sushi:                       quick previewer for nautilus

	package_install \
		alacarte \
		baobab \
		cheese \
		dconf-editor \
		eog \
		evince \
		file-roller \
		gnome-calculator \
		gnome-characters \
		gnome-clocks \
		gnome-control-center \
		gnome-disk-utility \
		gnome-font-viewer \
		gnome-keyring \
		gnome-logs \
		gnome-screenshot \
		gnome-system-monitor \
		gnome-tweaks \
		gpick \
		nautilus \
		sushi
}

setup_grub() {
	sudo sed -i '/GRUB_TIMEOUT=/c\GRUB_TIMEOUT=1' /etc/default/grub
	sudo sed -i '/GRUB_TIMEOUT_STYLE=/c\GRUB_TIMEOUT_STYLE=hidden' /etc/default/grub

	sudo grub-mkconfig -o /boot/grub/grub.cfg
}

setup_gsmartcontrol() {
	# disk health checker
	package_install gsmartcontrol
}

setup_keyboard() {
	# Korean keyboard support
	package_install ibus-hangul

	POST_INSTALL+=("keyboard: setup korean keyboard and reboot")
}

setup_middleclickpaste() {
	# prevents middle click paste
	package_install xmousepasteblock-git

	# todo: make it autostart
}

setup_pacman() {
	# enable multilib, color, parallel download, and total download in /etc/pacman.conf
	:
}

setup_pamac() {
	smart_mkdir "$SCRIPT_DIR/tmp"

	cd "$SCRIPT_DIR/tmp" || (error "failed to move to $SCRIPT_DIR/tmp for pamac installation" && exit 1)
	sudo pacman --noconfirm -S --needed git
	git clone https://aur.archlinux.org/libpamac-aur.git
	cd ./libpamac-aur && makepkg -si

	cd "$SCRIPT_DIR/tmp" || (error "failed to move to $SCRIPT_DIR/tmp for pamac installation" && exit 1)
	git clone https://aur.archlinux.org/pamac-aur.git
	cd ./pamac-aur && makepkg -si

	cd "$SCRIPT_DIR" || (error "failed to come back to working directory after installing pamac" && exit 1)

	# idk why but the permissions is set like this
	sudo install -g root -o root -m u=rwx,g=rx,o=rx ./etc/pamac.conf /etc/pamac.conf
	sudo install -g root -o root -m u=rw,g=r,o=r ./etc/pacman.conf /etc/pacman.conf

	sudo pacman -Syyuu
}

setup_pavucontrol() {
	# PulseAudio settings I use for redirecting desktop audio to microphone input
	package_install pavucontrol
}

setup_pomky() {
	install ./home/pomp/.local/bin/pomky ~/.local/bin/
	install ./home/pomp/.config/autostart/pomky.desktop ~/.config/autostart/
}

setup_shfmt() {
	package_install shfmt
}

setup_steam() {
	package_install steam
}

setup_timeshift() {
	# backup and restore system
	package_install timeshift
}

setup_vim() {
	# vim plugin manager
	package_install vim-plug

	install ./home/pomp/.vimrc ~
	POST_INSTALL+=("Install vim plugins with :PlugInstall command")
}

setup_wine() {
	# wine:       compatibility layer
	# wine-gecko: internet explorer for wine
	# wine-mono:  .NET runtime for wine
	# winetricks: wine helper script

	package_install \
		wine \
		wine-gecko \
		wine-mono \
		winetricks

	# WINEARCH=win32 WINEPREFIX=~/.win32/ winecfg
	# winetricks allfonts
	# winetricks settings fontsmooth=rgb
}

dnspy
"""
