#!/bin/bash

# don't remove line after yay_install or pacman_install
# it will result in this syntax error: unexpected end of file

# #################### [ ESSENTIALS ] ####################
# Installs essential packages and defining important functions

# https://stackoverflow.com/a/246128/12979111
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR

BOLD="\e[1m"
DIM="\e[2m"
UNDERLINE="\e[4m"
INVERT="\e[7m"
RESET="\e[0m"

RED="\e[91m"  # actually light red
GREEN="\e[92m"  # actually light green
YELLOW="\e[33m"

log_no_label() {
	echo -e "$GREEN$BOLD$@$RESET"
}

warn_no_label() {
	echo -e "$YELLOW$BOLD$@$RESET"
}

error_no_label() {
	echo -e "$RED$BOLD$@$RESET"
}

log() {
	echo -e " $GREEN$BOLD    INFO |  $@$RESET"
}

warn() {
	echo -e " $YELLOW$BOLD WARNING |  $@$RESET"
}

error() {
	>&2 echo -e " $RED$BOLD   ERROR |  $@$RESET"
}

title() {
	echo
	echo -e "$BOLD$GREEN====================[ $@ ]====================$RESET"
}

pacman_install() {
	sudo pacman -S --needed --noconfirm $@
}

yay_install() {
	# install a AUR package if it's not already installed

	for package_name in "$@"; do
		if ! yay -Qi $package_name > /dev/null 2>&1 ; then
			log "yay: installing \"$package_name\""
			yay -S --answerclean None --answerdiff None --answeredit None --aur $package_name
		fi
	done
	exit
}

# #################### [ DEFINING ESSENTIAL SETUP ] ####################

backup() {
	dconf dump / > $SCRIPT_DIR/dconf.conf
	# copy /home/pomp directory
	# timeshift settings
	sudo timeshift --create --comments "auto created by developomp setup script"
}

setup_essentials() {
	:
	# enable multilib, color, parallel download, and total download in /etc/pacman.conf
}

install_essentials() {
	# install yay if it's not installed
	if ! command -v yay &> /dev/null; then
		sudo pacman -S --needed --noconfirm git base-devel
		git clone https://aur.archlinux.org/yay.git
		cd yay
		makepkg -si
		cd $SCRIPT_DIR
	fi

	yay_install \
		4kvideodownloader                  `# downloading videos and audio from youtube` \
		figma-linux-font-helper            `# using local fonts in figma` \
		grive                              `# google drive syncing` \
		gwe                                `# nvidia GPU overclocking` \
		jdk                                `# java development` \
		mystiq                             `# video conversion` \
		obs-input-overlay-bin              `# show inputs in OBS` \
		osu-lazer                          `# Rhythm game` \
		pamac-aur                          `# GUI for arch package management` \
		timeshift                          `# system backup` \
		unityhub                           `# game development` \
		visual-studio-code-bin             `# programming & text editing` \
		xinput-gui                         `# A simple GUI for Xorg's Xinput tool` \
		xmousepasteblock-git               `# force disable middle click paste` \
		zoom                               `# video conference` \
		matcha-gtk-theme                   `# gtk theme` \

	pacman_install \
		alacarte                           `# editing apps in gnome menu` \
		audacity                           `# editing audio` \
		blender                            `# 3D modeling, simulations, and video editing` \
		conky                              `# system monitoring` \
		dotnet-sdk                         `# C# development (for unity)` \
		filezilla                          `# FTP client` \
		firefox-developer-edition          `# browser` \
		gimp                               `# image editing` \
		git                                `# version control system` \
		go                                 `# golang development` \
		gpa                                `# PGP key management` \
		gpick                              `# screen color picking` \
		gsmartcontrol                      `# SSD health check` \
		hardinfo                           `# seeing system hardware information` \
		htop                               `# managing processes` \
		ibus-hangul                        `# ` \
		inkscape                           `# vector editing tool` \
		intellij-idea-community-edition    `# java development` \
		lldb                               `# debugger` \
		networkmanager                     `# Network connection manager` \
		nodejs                             `# ` \
		npm                                `# javascript development` \
		obs-studio                         `# screen recording and streaming` \
		pavucontrol                        `# ` \
		piper                              `# changing gaming mouse settings` \
		putty                              `# ` \
		python-pip                         `# python package management` \
		ranger                             `# CLI File manager` \
		sqlitebrowser                      `# ` \
		steam                              `# ` \
		steam-native-runtime               `# ` \
		sudo                               `# To run commands as root` \
		tmux                               `# running task independent of session` \
		transmission-gtk                   `# ` \
		vim                                `# the good text editor` \
		vlc                                `# audio & video playback` \
		vnstat                             `# network traffic statistics (for conky)` \
		wine                               `# ` \
		wine-gecko                         `# ` \
		wine-mono                          `# ` \
		winetricks                         `# ` \
		wireshark                          `# ` \
		yarn                               `# ` \

}

# #################### [ DEFINING SETUP ] ####################
# Define instructions on how to setup applications & stuff
# Assumes all essential packages are installed already (git, vim, etc.)

setup_gnome() {
	pacman_install \
		baobab                    `# Disk usage analysis` \
		cheese                    `# Capturing photo / video with webcam` \
		dconf-editor              `# GUI for dconf` \
		eog                       `# image viewer` \
		evince                    `# document viewer` \
		file-roller               `# compression and decompression` \
		gedit                     `# text editing when nautilus is on admin mode` \
		gnome-calculator          `# Quick calculation` \
		gnome-characters          `# Search for emojis, special characters, and symbols` \
		gnome-clocks              `# For multiple clocks for different time zones` \
		gnome-control-center      `# Essential settings` \
		gnome-disk-utility        `# Disk management` \
		gnome-font-viewer         `# Managing fonts` \
		gnome-keyring             `# Store passwords and keys` \
		gnome-logs                `# GUI for system journal` \
		gnome-screenshot          `# Quick screenshot` \
		gnome-shell               `# Graphical interface` \
		gnome-shell-extensions    `# Extensions for gnome` \
		gnome-system-monitor      `# Process management` \
		gnome-terminal            `# Terminal emulation` \
		gnome-tweaks              `# Advanced settings` \
		gnome-usage               `# System resource statistics` \
		mutter                    `# window manager` \
		nautilus                  `# File management` \
		simple-scan               `# Scanning utility` \

	yay_install \
		gnome-terminal-transparency            `# Transparent gnome terminal` \
		gnome-shell-extension-installer        `# Installation of gnome extensions from command line` \
		gnome-shell-extension-pop-shell-git    `# switching between stacked mode and tiling mode` \

	# install gnome extensions
	echo "installing gnome extensions"
	extension_ids=(
		36    # lock-keys
		131   # touchpad-indicator
		355   # status-area-horizontal-spacing
		657   # shelltile
		750   # openweather
		800   # remove-dropdown-arrows
		841   # freon
		906   # sound-output-device-chooser
		945   # cpu-power-manager
		2741  # remove-alttab-delay-v2
		2890  # tray-icons-reloaded
		4000  # babar
	)
	
	echo "Installing:"
	for extension_id in "${extension_ids[@]}"; do
		echo "- https://extensions.gnome.org/extension/$extension_id"
		gnome-shell-extension-installer --yes $extension_id
	done

	echo "Restarting gnome shell"
	killall -3 gnome-shell
}

setup_discord() {
	pacman_install discord

	yay_install \
	betterdiscord-installer    `# installer for betterdiscord` \
	discord-overlay-git        `# overlay for discord` \

	# BD plugins
	# https://betterdiscord.app/plugin/Avatar%20Hover
	# https://betterdiscord.app/plugin/BadgesEverywhere
	# https://betterdiscord.app/plugin/BetterCodeblocks
	# https://betterdiscord.app/plugin/BetterNsfwTag
	# https://betterdiscord.app/plugin/BetterSearchPage
	# https://betterdiscord.app/plugin/CallTimeCounter
	# https://betterdiscord.app/plugin/CharCounter
	# https://betterdiscord.app/plugin/CompleteTimestamps
	# https://betterdiscord.app/plugin/Copier
	# https://betterdiscord.app/plugin/CopyRawMessage
	# https://betterdiscord.app/plugin/CreationDate
	# https://betterdiscord.app/plugin/DoNotTrack
	# https://betterdiscord.app/plugin/EmoteReplacer
	# https://betterdiscord.app/plugin/FreeEmojis
	# https://betterdiscord.app/plugin/GoogleTranslateOption
	# https://betterdiscord.app/plugin/GrammarCorrect
	# https://betterdiscord.app/plugin/GuildProfile
	# https://betterdiscord.app/plugin/ImageUtilities
	# https://betterdiscord.app/plugin/InvisibleTyping
	# https://betterdiscord.app/plugin/JoinedAtDate
	# https://betterdiscord.app/plugin/LastMessageDate
	# https://betterdiscord.app/plugin/Link-Profile-Picture
	# https://betterdiscord.app/plugin/MemberCount
	# https://betterdiscord.app/plugin/PermissionsViewer
	# https://betterdiscord.app/plugin/PlatformIndicators
	# https://betterdiscord.app/plugin/QuickMention
	# https://betterdiscord.app/plugin/RedditMentions
	# https://betterdiscord.app/plugin/RevealAllSpoilersOption
	# https://betterdiscord.app/plugin/SecretRingTone
	# https://betterdiscord.app/plugin/SendLargeMessages
	# https://betterdiscord.app/plugin/ServerCounter
	# https://betterdiscord.app/plugin/ShowAllActivities
	# https://betterdiscord.app/plugin/ShowConnections
	# https://betterdiscord.app/plugin/ShowHiddenChannels
	# https://betterdiscord.app/plugin/SpellCheck
	# https://betterdiscord.app/plugin/StaffTag
	# https://betterdiscord.app/plugin/SuppressReplyMentions
	# https://betterdiscord.app/plugin/Typing%20Users%20Avatars
	# https://betterdiscord.app/plugin/TypingIndicator
	# https://betterdiscord.app/plugin/UserDetails
}

setup_cpu_undervolting() {
	# Undervolting for intel CPU
	# https://wiki.archlinux.org/index.php/Undervolting_CPU

	pacman_install intel-undervolt

	config_file=/etc/intel-undervolt.conf

	# create backup in case anything goes wrong
	sudo cp $config_file $config_file.bak

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

setup_font() {
	echo "installing fonts"
	
	# path to temporarily save font related files
	fonts_directory="./fonts"

	# fonts to download
	font_names=(
		"Audiowide"
		"Comfortaa"
		"Nanum Gothic"
		"Source Code Pro"
	)

	# create fonts directory if it does not exist
	if [ ! -d "$fonts_directory" ]; then
		mkdir "$fonts_directory"
	fi

	# download and unzip font files if they're not downloaded already
	for font_name in "${font_names[@]}"; do
		zip_path="$fonts_directory/$font_name.zip"

		# download and unzip if either zip file or unzipped directory exists
		if [ ! -f "$zip_path" ] && [ ! -d "$fonts_directory/$font_name" ]; then
			wget -O "$zip_path" "https://fonts.google.com/download?family=$font_name"  # download zip file
			unzip "$zip_path" -d "$fonts_directory/$font_name"  # unzip file
			rm "$zip_path"  # remove zip file
		fi
	done
	
	font_install_dir="$HOME/.local/share/fonts"

	# create local fonts directory if it does not exist already
	if [ ! -d "$font_install_dir" ]; then
		mkdir "$font_install_dir"
	fi

	# "install" all fonts
	find "$fonts_directory" -type f -name "*.ttf" | while read ttf_file_path ; do
		mv -f "$ttf_file_path" "$font_install_dir/${ttf_file_path##*/}"
	done

	# regenerate font cache
	fc-cache -vf

	# cleanup
	rm -rf $fonts_directory

	pacman_install \
		noto-fonts-emoji    `# ` \

	yay_install \
		ttf-wps-fonts                `# ` \
		ttf-ms-win10                 `# ` \
		nerd-fonts-noto-sans-mono    `# Terminal font` \

}

setup_pamac() {
	:
	# enable AUR package.
}

setup_wireshart() {
	:
	sudo usermod -a -G wireshark $USER
}

setup_middleclickpaste() {
	:
	# make it autostart
}

setup_node() {
	:
	# https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
	# export PATH="$(yarn global bin):$PATH"
}

setup_pamac() {
	:
	# enable AUR on pamac
}

setup_dns() {
	:
	# https://1.1.1.1
}

setup_unity() {
	yay_install unityhub

	# editors location for unity hub (`/media/pomp/data/programs/Unity Hub/Unity Editors`)
	# vscode setup
}

setup_virtualbox() {
	# https://wiki.archlinux.org/title/VirtualBox

	pacman_install \
		virtualbox                      `# OS emulation` \
		virtualbox-host-modules-arch    `# ` \
		virtualbox-guest-iso            `# ` \
	
	yay_install virtualbox-ext-oracle

	sudo vboxreload
	sudo modprobe vboxdrv
}

setup_optimus_manager() {
	# Not using power switching
	# read this wiki[1] about power management with acpi call for more information
	# [1] https://github.com/Askannz/optimus-manager/wiki/A-guide--to-power-management-options#configuration-4--acpi_call

	yay_install \
		gwe                   `# https://gitlab.com/leinardi/gwe` \
		optimus-manager       `# https://github.com/Askannz/optimus-manager` \
		optimus-manager-qt    `# https://github.com/Shatur/optimus-manager-qt` \

	# launch on startup
	# nvidia as default

	# Performance: 265, 750
	# Energy Saver: -155, -365
}

setup_minecraft() {
	yay_install \
		minecraft-launcher      `# ` \
		worldpainter            `# ` \
		minecraft-overviewer    `# ` \

	# mcaselector (/usr/lib/jvm/java-15-openjdk/bin/java --module-path /media/pomp/data/master_folder/programming/java/javafx-sdk-16/lib --add-modules ALL-MODULE-PATH -jar /usr/share/java/mcaselector.jar)
}

setup_user_directories() {
	pacman_install xdg-user-dirs

	# edit `~/.config/user-dirs.dirs`:

	# XDG_DESKTOP_DIR="$HOME/Desktop"
	# XDG_DOWNLOAD_DIR="/media/pomp/data/Downloads"
	# XDG_TEMPLATES_DIR="$HOME/Templates"
	# XDG_PUBLICSHARE_DIR="$HOME/Public"
	# XDG_DOCUMENTS_DIR="/media/pomp/data/google-drive/Documents"
	# XDG_MUSIC_DIR="/media/pomp/data/google-drive/Music"
	# XDG_PICTURES_DIR="/media/pomp/data/google-drive/Pictures"
	# XDG_VIDEOS_DIR="/media/pomp/data/Videos"

}

setup_wine() {
	pacman_install \
		wine \

	# - wine-mono
	# - winetricks
	# - wine-gecko

	# - `WINEARCH=win32 WINEPREFIX=~/.win32/ winecfg`
	# - `winetricks allfonts`
	# - `winetricks settings fontsmooth=rgb`
}

setup_nvidia() {
	# https://wiki.archlinux.org/title/NVIDIA
	# https://wiki.archlinux.org/title/Vulkan

	pacman_install \
		cuda                       `# ` \
		cuda-tools                 `# ` \
		lib32-nvidia-utils         `# ` \
		lib32-vulkan-icd-loader    `# ` \
		nvidia                     `# ` \
		nvidia-settings            `# ` \
		nvidia-utils               `# ` \
		vulkan-icd-loader          `# ` \

}

setup_steam() {
	#https://wiki.archlinux.org/title/Steam

	pacman_install steam

	# change steam library directory (/media/pomp/data/programs/SteamLibrary)
	# enable steam proton play
}

setup_conky() {
	pacman_install \
		conky     `# ` \
		vnstat    `# ` \

	# enable on startup
	# sudo systemctl enable vnstat
	# sudo systemctl start vnstat
}

setup_dconf() {
	# todo: freon GPU, decimal, and unit
	# must be done after install to make sure configs are not overwritten
	dconf load / < $SCRIPT_DIR/dconf.conf
}

setup_local() {
	# setup for applications in second drive
	# add to application menu
	# office 2019 wine

	if [[ -d /media/pomp/data/programs/dnSpy-net-win32 ]]; then
		echo "dnspy"
	fi

	if [[ -d /media/pomp/data/programs/amidst ]]; then
		echo "amidst"
	fi

	if [[ -d /media/pomp/data/programs/mcaselector ]]; then
		echo "mcaselector"
	fi

	if [[ -d /media/pomp/data/programs/mineways ]]; then
		echo "mineways"
	fi

	if [[ -d /media/pomp/data/programs/tor-browser ]]; then
		echo "tor"
	fi
}

setup_plymouth() {
	# must be done after optimus
	# https://wiki.archlinux.org/title/plymouth

	yay_install \
		plymouth                    `# ` \
		gdm-plymouth-prime          `# ` \
		plymouth-theme-arch-logo    `# ` \

}

setup_grub_theme() {
	# only show when esc is pressed
	# check how manjaro did it
	pacman_install grub-theme-vimix
}

setup_kdenlive() {
	:
	# Use appimage package
	# no kde dependencies
}





# #################### [ START ] ####################

warn_no_label "This is not a completely hands off process."
warn_no_label "You need to monitor the process and take appropriate actions."
echo

# https://stackoverflow.com/a/1885534/12979111
read -p "Press (y) to continue. Press (any other key) to exit. " -n 1 -r
if [[ $REPLY =~ ^[^Yy]$ ]]; then
	echo
    log "canceled"
	exit
fi

echo

# #################### [ TESTING ] ####################
# Tests if script is ready to be executed
# some stuff has to be done manually

title "TESTING"
log "working directory: $RESET$BOLD$PWD"

log "checking if script is running with root privilege"
if [[ ! $EUID -ne 0 ]]; then
	error "DO NOT RUN THIS SCRIPT AS ROOT"
	exit 1
fi

log "checking if sudo exists"
if ! command -v sudo &> /dev/null; then
    error "cannot find sudo!"
    exit 1
fi

log "checking partition"

log "checking if $RESET$BOLD/media/pomp/data$GREEN exists in fstab and mounted"

log "checking if OS is arch"
# log "no manjaro support"

log "checking if grub is installed and set up properly"

echo
log "TESTING phase complete!"

# #################### [ MAIN ] ####################
# this is not a hands-free operation blah blah

run_install() {
	install_essentials
}

post_install() {
	echo "login firefox & vscode"
	echo "restore onetab"
	echo "reboot using poweroff"
	echo "gnome korean keyboard"
	echo "sign into vscode"
	echo "EDITOR=vim sudo visudo"
	echo "Defaults pwfeedback"
}

title "DONE"
