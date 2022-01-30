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

setup_discord() {
	# assumes that plugins are located in ~/.config/BetterDiscord/plugins

	# betterdiscordctl-git: BetterDiscord installer

	package_install \
		discord \
		betterdiscordctl-git

	install ./home/pomp/.config/autostart/discord.desktop ~/.config/autostart/

	BD_PLUGINS=(
		134 # https://betterdiscord.app/plugin/Avatar%20Hover
		60  # https://betterdiscord.app/plugin/BadgesEverywhere
		119 # https://betterdiscord.app/plugin/BetterCodeblocks
		62  # https://betterdiscord.app/plugin/BetterNsfwTag
		63  # https://betterdiscord.app/plugin/BetterSearchPage
		228 # https://betterdiscord.app/plugin/CallTimeCounter
		64  # https://betterdiscord.app/plugin/CharCounter
		67  # https://betterdiscord.app/plugin/CompleteTimestamps
		176 # https://betterdiscord.app/plugin/Copier
		68  # https://betterdiscord.app/plugin/CopyRawMessage
		69  # https://betterdiscord.app/plugin/CreationDate
		186 # https://betterdiscord.app/plugin/DoNotTrack
		132 # https://betterdiscord.app/plugin/EmoteReplacer
		245 # https://betterdiscord.app/plugin/FreeEmojis
		81  # https://betterdiscord.app/plugin/GoogleTranslateOption
		284 # https://betterdiscord.app/plugin/GrammarCorrect
		220 # https://betterdiscord.app/plugin/GuildProfile
		83  # https://betterdiscord.app/plugin/ImageUtilities
		295 # https://betterdiscord.app/plugin/InvisibleTyping
		84  # https://betterdiscord.app/plugin/JoinedAtDate
		85  # https://betterdiscord.app/plugin/LastMessageDate
		287 # https://betterdiscord.app/plugin/Link-Profile-Picture
		11  # https://betterdiscord.app/plugin/MemberCount
		29  # https://betterdiscord.app/plugin/PermissionsViewer
		158 # https://betterdiscord.app/plugin/PlatformIndicators
		93  # https://betterdiscord.app/plugin/QuickMention
		94  # https://betterdiscord.app/plugin/ReadAllNotificationsButton
		179 # https://betterdiscord.app/plugin/RedditMentions
		97  # https://betterdiscord.app/plugin/RevealAllSpoilersOption
		98  # https://betterdiscord.app/plugin/SendLargeMessages
		159 # https://betterdiscord.app/plugin/ShowAllActivities
		291 # https://betterdiscord.app/plugin/ShowConnections
		103 # https://betterdiscord.app/plugin/ShowHiddenChannels
		104 # https://betterdiscord.app/plugin/SpellCheck
		162 # https://betterdiscord.app/plugin/StaffTag
		8   # https://betterdiscord.app/plugin/SuppressReplyMentions
		253 # https://betterdiscord.app/plugin/Typing%20Users%20Avatars
		196 # https://betterdiscord.app/plugin/TypingIndicator
		293 # https://betterdiscord.app/plugin/UserDetails
	)

	log "installing betterdiscord plugins"

	for id in "${BD_PLUGINS[@]}"; do
		BD_PLUGIN_URL="https://betterdiscord.app/Download?id=$id"
		log "installing $BD_PLUGIN_URL"
		wget --content-disposition --no-clobber -P ~/.config/BetterDiscord/plugins "$BD_PLUGIN_URL"
	done

	POST_INSTALL+=("discord: run betterdiscordctl install")
}

setup_docker() {
	package_install docker

	sudo usermod -aG docker "${USER}"
	sudo systemctl --now enable docker
}

setup_filezilla() {
	package_install filezilla
}

setup_fonts() {
	log "installing fonts"

	# wget:                             For downloading zip files
	# noto-fonts-emoji:                 Emoji fonts
	# nerd-fonts-noto-sans-mono:        Terminal font
	# ttf-baekmuk:                      Korean font

	package_install \
		wget \
		noto-fonts-emoji \
		nerd-fonts-noto-sans-mono \
		ttf-baekmuk

	# path to temporarily save font related files
	fonts_directory="$SCRIPT_DIR/tmp/fonts"

	# fonts to download
	font_names=(
		"Audiowide"
		"Varela Round"
		"Ubuntu Mono"
		"Nanum Gothic Coding"
	)

	# create fonts directory if it does not exist
	if [ ! -d "$fonts_directory" ]; then
		mkdir -p "$fonts_directory"
	fi

	# download and unzip font files if they're not downloaded already
	for font_name in "${font_names[@]}"; do
		zip_path="$fonts_directory/$font_name.zip"

		# download and unzip if either zip file or unzipped directory exists
		if [ ! -f "$zip_path" ] && [ ! -d "$fonts_directory/$font_name" ]; then
			wget -O "$zip_path" "https://fonts.google.com/download?family=$font_name" # download zip file
			unzip "$zip_path" -d "$fonts_directory/$font_name"                        # unzip file
			rm "$zip_path"                                                            # remove zip file
		fi
	done

	font_install_dir="$HOME/.local/share/fonts"

	# create local fonts directory if it does not exist already
	if [ ! -d "$font_install_dir" ]; then
		mkdir -p "$font_install_dir"
	fi

	# "install" all fonts
	find "$fonts_directory" -type f -name "*.ttf" | while read ttf_file_path; do
		mv -f "$ttf_file_path" "$font_install_dir/${ttf_file_path##*/}"
	done

	# regenerate font cache
	fc-cache -vf

	# cleanup
	rm -rf $fonts_directory
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

setup_gnome_extensions() {
	log "installing gnome extensions"

	# chrome-gnome-shell                     GNOME shell integration for Chrome
	# gnome-shell-extension-installer        Installation of gnome extensions from command line
	# gnome-shell-extension-pop-shell-git    for window tiling
	package_install \
		chrome-gnome-shell \
		gnome-shell-extension-installer \
		gnome-shell-extension-pop-shell-git

	load_dconf "extension-pop-shell.conf"

	extensions=(
		36,"extension-lockkeys.conf"                     # lock-keys
		906,"extension-sound-output-device-chooser.conf" # sound-output-device-chooser
		1460,"extension-vitals.conf"                     # vitals
		2741,""                                          # remove-alttab-delay-v2
		2890,"extension-trayIconsReloaded.conf"          # tray-icons-reloaded
		3193,"extension-blur-my-shell.conf"              # blur-my-shell
		4000,"extension-barbar.conf"                     # babar
		4158,""                                          # gnome-40-ui-improvements
	)

	for i in "${extensions[@]}"; do
		IFS=","
		set -- $i

		# $1: extension id
		# $2: extension dconf

		log "installing: https://extensions.gnome.org/extension/$1"
		gnome-shell-extension-installer $1 --yes --update

		if [ ! -z $2 ]; then
			load_dconf $2
		fi
	done

	# enable extensions
	load_dconf "extensions.conf"

	gnome-shell-extension-installer --restart-shell
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

setup_mystiq() {
	# video converter
	package_install mystiq
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

setup_pip() {
	# package installer for python
	package_install python-pip
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
