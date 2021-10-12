#!/bin/bash

# don't remove line after package_install
# it will result in this syntax error: unexpected end of file


# #################### [ ESSENTIALS ] ####################
# Installs essential packages and defining important functions

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
DATA_PATH="/media/pomp/data"
POST_INSTALL=()

BOLD="\e[1m"
RESET="\e[0m"

RED="\e[91m"  # actually light red
GREEN="\e[92m"  # actually light green
YELLOW="\e[33m"

log_no_label() {
	echo -e "$GREEN$BOLD$*$RESET"
}

warn_no_label() {
	echo -e "$YELLOW$BOLD$*$RESET"
}

error_no_label() {
	echo -e "$RED$BOLD$*$RESET"
}

log() {
	echo -e " $GREEN$BOLD    INFO |  $*$RESET"
}

warn() {
	echo -e " $YELLOW$BOLD WARNING |  $*$RESET"
}

error() {
	>&2 echo -e " $RED$BOLD   ERROR |  $*$RESET"
}

title() {
	echo
	echo -e "$BOLD$GREEN====================[ $* ]====================$RESET"
}

smart_mkdir() {
	# make directory recursively if it doesn't exist already

	if [ ! -d "$1" ]; then
		mkdir -p "$1"
	fi
}

package_install() {
	pamac install --no-confirm "$@"
}

package_remove() {
	pamac remove --no-confirm "$@"
}

setup_essentials() {
	# install pamac if it does not exist
	if ! command -v pamac &> /dev/null; then
		log "pamac was not installed already. Installing now..."
		setup_pamac
	fi

	# install dialog if it's not installed already
	if ! command -v dialog &> /dev/null; then
		log "dialog was not installed already. Installing now..."
		package_install dialog
	fi
}

load_dconf() {
	dconf load / < "./dconf/$1"
}


# #################### [ DEFINING SETUP ] ####################
# Define instructions on how to setup applications & stuff

setup_4kvideodownloader() {
	package_install       \
		4kvideodownloader \

}

setup_blender() {
	package_install \
		blender     \

}

setup_brave() {
	package_install        \
		brave-beta-browser \

	# settings: DNS https cloudflare
	POST_INSTALL+=(
		"brave: sync device"
		"brave: restore onetab"
	)
}

setup_conky() {
	cp ./.conky/ ~
	cp ./autostart/conky.desktop ~/.config/autostart

	package_install                              \
		conky                                    \
		vnstat    `# network traffic statistics` \

	sudo systemctl enable vnstat
	sudo systemctl start vnstat
}

setup_cpu_undervolting() {
	# Undervolting for intel CPU
	# https://wiki.archlinux.org/index.php/Undervolting_CPU

	package_install                                                                  \
		intel-undervolt    `# CPU undervolting for less heat and power consumption` \

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

setup_dconf() {
	:
	# must be done after install to make sure configs are not overwritten
	# dconf load / < dconf/configuration.conf
}

setup_discord() {
	# assumes that plugins are located in ~/.config/BetterDiscord/plugins

	package_install                                            \
		discord                                                \
		betterdiscordctl-git    `# BetterDiscord installer`    \
		discord-overlay-git     `# Discord voice chat overlay` \

	betterdiscordctl install

	BD_PLUGINS=(
		134    # https://betterdiscord.app/plugin/Avatar%20Hover
		60     # https://betterdiscord.app/plugin/BadgesEverywhere
		119    # https://betterdiscord.app/plugin/BetterCodeblocks
		62     # https://betterdiscord.app/plugin/BetterNsfwTag
		63     # https://betterdiscord.app/plugin/BetterSearchPage
		228    # https://betterdiscord.app/plugin/CallTimeCounter
		64     # https://betterdiscord.app/plugin/CharCounter
		67     # https://betterdiscord.app/plugin/CompleteTimestamps
		176    # https://betterdiscord.app/plugin/Copier
		68     # https://betterdiscord.app/plugin/CopyRawMessage
		69     # https://betterdiscord.app/plugin/CreationDate
		186    # https://betterdiscord.app/plugin/DoNotTrack
		132    # https://betterdiscord.app/plugin/EmoteReplacer
		245    # https://betterdiscord.app/plugin/FreeEmojis
		81     # https://betterdiscord.app/plugin/GoogleTranslateOption
		284    # https://betterdiscord.app/plugin/GrammarCorrect
		220    # https://betterdiscord.app/plugin/GuildProfile
		83     # https://betterdiscord.app/plugin/ImageUtilities
		295    # https://betterdiscord.app/plugin/InvisibleTyping
		84     # https://betterdiscord.app/plugin/JoinedAtDate
		85     # https://betterdiscord.app/plugin/LastMessageDate
		287    # https://betterdiscord.app/plugin/Link-Profile-Picture
		11     # https://betterdiscord.app/plugin/MemberCount
		29     # https://betterdiscord.app/plugin/PermissionsViewer
		158    # https://betterdiscord.app/plugin/PlatformIndicators
		93     # https://betterdiscord.app/plugin/QuickMention
		94     # https://betterdiscord.app/plugin/ReadAllNotificationsButton
		179    # https://betterdiscord.app/plugin/RedditMentions
		97     # https://betterdiscord.app/plugin/RevealAllSpoilersOption
		139    # https://betterdiscord.app/plugin/SecretRingTone
		98     # https://betterdiscord.app/plugin/SendLargeMessages
		99     # https://betterdiscord.app/plugin/ServerCounter
		159    # https://betterdiscord.app/plugin/ShowAllActivities
		291    # https://betterdiscord.app/plugin/ShowConnections
		103	   # https://betterdiscord.app/plugin/ShowHiddenChannels
		104    # https://betterdiscord.app/plugin/SpellCheck
		162    # https://betterdiscord.app/plugin/StaffTag
		8      # https://betterdiscord.app/plugin/SuppressReplyMentions
		253    # https://betterdiscord.app/plugin/Typing%20Users%20Avatars
		196    # https://betterdiscord.app/plugin/TypingIndicator
		293    # https://betterdiscord.app/plugin/UserDetails
	)

	log "installing betterdiscord plugins"

	for id in "${BD_PLUGINS[@]}"; do
		BD_PLUGIN_URL="https://betterdiscord.app/Download?id=$id"
		log "installing $BD_PLUGIN_URL"
		wget --content-disposition --no-clobber -P ~/.config/BetterDiscord/plugins "$BD_PLUGIN_URL"
	done
}

setup_dotnet() {
	package_install                \
		dotnet-sdk    `# .NET SDK` \

}

setup_fonts() {
	log "installing fonts"

	# path to temporarily save font related files
	fonts_directory="$SCRIPT_DIR/tmp/fonts"

	# fonts to download
	font_names=(
		"Audiowide"
		"Comfortaa"
		"Nanum Gothic"
		"Source Code Pro"
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
			wget -O "$zip_path" "https://fonts.google.com/download?family=$font_name"  # download zip file
			unzip "$zip_path" -d "$fonts_directory/$font_name"  # unzip file
			rm "$zip_path"  # remove zip file
		fi
	done
	
	font_install_dir="$HOME/.local/share/fonts"

	# create local fonts directory if it does not exist already
	if [ ! -d "$font_install_dir" ]; then
		mkdir -p "$font_install_dir"
	fi

	# "install" all fonts
	find "$fonts_directory" -type f -name "*.ttf" | while read ttf_file_path ; do
		mv -f "$ttf_file_path" "$font_install_dir/${ttf_file_path##*/}"
	done

	# regenerate font cache
	fc-cache -vf

	# cleanup
	rm -rf $fonts_directory

	package_install                                         \
		noto-fonts-emoji                                    \
		nerd-fonts-noto-sans-mono         `# Terminal font` \
		adobe-source-han-sans-kr-fonts    `# Korean font`   \
		ttf-baekmuk                       `# Korean font`   \

}

setup_dns() {
	:
	# https://1.1.1.1
}

setup_gimp() {
	package_install                    \
		gimp    `# photoshop but FOSS` \

}

setup_gnome() {
	# gnome, nvidia driver, and optimus manager

	# install gnome
	package_install                                                                           \
		gdm-prime                 `# gdm patched for optimus laptops`                         \
		xcursor-breeze            `# cursor design`                                           \
		matcha-gtk-theme          `# gtk theme`                                               \
		papirus-icon-theme        `# icon theme`                                              \
		gnome-backgrounds         `# wallpapers and shit`                                     \
		gnome-shell-extensions    `# gnome shell extensions`                                  \
		gwe                       `# nvidia GPU overclocking https://gitlab.com/leinardi/gwe` \
		nvidia                    `# nvidia GPU support`                                      \
		optimus-manager-qt        `# https://github.com/Shatur/optimus-manager-qt`            \

	# prevent rootless X
	cp ./Xwrapper.config /etc/X11/
	load_dconf "gnome-desktop-interface.conf"
	sudo systemctl enable gdm
	sudo systemctl enable optimus-manager

	setup_gnome_apps

	cat > ~/.config/user-dirs.dirs <<EOL
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

	# todo: auto start optimus on login
	# todo: optimus set nvidia as default

	# todo: add profile (Performance: 250, 650)

	POST_INSTALL+=("gnome: reboot")
}

setup_gnome_apps() {
	# install gnome apps
	package_install                                                                              \
		alacarte                       `# application menu editor`                               \
		baobab                         `# Disk usage analysis`                                   \
		cheese                         `# take photo/video with camera`                          \
		dconf-editor                   `# GUI for dconf`                                         \
		eog                            `# photo viewer`                                          \
		evince                         `# document viewer`                                       \
		file-roller                    `# compress & decompress files/directories`               \
		gnome-calculator               `# scientific calculator`                                 \
		gnome-characters               `# Search for emojis, special characters, and symbols`    \
		gnome-clocks                   `# For multiple clocks for different time zones`          \
		gnome-control-center           `# gnome settings`                                        \
		gnome-disk-utility             `# gnome disk management`                                 \
		gnome-font-viewer              `# Managing fonts`                                        \
		gnome-keyring                  `# passwords and keys`                                    \
		gnome-logs                     `# GUI for systemd journal`                               \
		gnome-screenshot               `# take screenshots`                                      \
		gnome-system-monitor           `# show system processes`                                 \
		gnome-terminal-transparency    `# Transparent gnome terminal`                            \
		gnome-tweaks                   `# shows extra settings`                                  \
		gpick                          `# color picker`                                          \
		nautilus                       `# gnome file manager`                                    \
		sushi                          `# quick previewer for nautilus`                          \

}

setup_gnome_extensions() {
	package_install                                                                               \
		gnome-shell-extension-installer        `# Installation of gnome extensions from command line` \
		gnome-shell-extension-pop-shell-git    `# for window tiling`                                  \

	# install gnome extensions
	log "installing gnome extensions"
	extension_ids=(
		36      # lock-keys
		355     # status-area-horizontal-spacing
		841     # freon
		906     # sound-output-device-chooser
		2741    # remove-alttab-delay-v2
		2890    # tray-icons-reloaded
		4000    # babar

		# waiting for gnome 40 support
		# 131     # touchpad-indicator
		# 800     # remove-dropdown-arrows
	)

	for extension_id in "${extension_ids[@]}"; do
		log "installing: https://extensions.gnome.org/extension/$extension_id"
		gnome-shell-extension-installer $extension_id
	done

	load_dconf "extension-barbar.conf"
	load_dconf "extension-freon.conf"
	load_dconf "extension-lockkeys.conf"
	load_dconf "extension-status-area-horizontal-spacing.conf"

	# todo: automate extension enabling
	POST_INSTALL+=("gnome: enable gnome extensions")
}

setup_go() {
	package_install \
		go          \

}

setup_godot() {
	package_install              \
		godot    `# game engine` \

}

setup_gsmartcontrol() {
	package_install                              \
		gsmartcontrol    `# disk health checker` \

}

setup_inkscape() {
	package_install                                \
		inkscape    `# adobe illustrator but FOSS` \

}

setup_kdenlive() {
	package_install                            \
		kdenlive-appimage    `# video editing` \

}

setup_keyboard() {
	package_install                                \
		ibus-hangul    `# Korean keyboard support` \

	POST_INSTALL+=("keyboard: setup korean keyboard and reboot")
}

setup_obs() {
	package_install                                                                                     \
		obs-plugin-input-overlay-bin    `# show inputs in OBS`                                          \
		obs-studio-browser              `# screen recording and streaming with browser overlay support` \

}

setup_osu() {
	# todo: enable multilib

	package_install                     \
		osu              `# osu stable` \

}

setup_middleclickpaste() {
	package_install                                             \
		xmousepasteblock-git    `# prevents middle click paste` \

	# todo: make it autostart
}

setup_mystiq() {
	package_install                   \
		mystiq    `# video converter` \

}

setup_node() {
	package_install                               \
		nodejs    `# Javascript on servers!`      \
		yarn      `# better node package manager` \

	# https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
	# export PATH="$(yarn global bin):$PATH"
}

setup_pacman() {
	# enable multilib, color, parallel download, and total download in /etc/pacman.conf
	:
}

setup_pamac() {
	smart_mkdir "$SCRIPT_DIR/tmp"
	cd "$SCRIPT_DIR/tmp" || (error "failed to move to $SCRIPT_DIR/tmp for pamac installation" && exit 1)
	sudo pacman --noconfirm -S --needed git
	git clone https://aur.archlinux.org/pamac-aur.git
	cd ./pamac-aur && makepkg -si

	cd "$SCRIPT_DIR" || (error "failed to come back to working directory after installing pamac" && exit 1)
}

setup_pavucontrol() {
	package_install                                                                                    \
		pavucontrol    `# PulseAudio settings I use for redirecting desktop audio to microphone input` \

}

setup_pip() {
	package_install                                    \
		python-pip    `# package installer for python` \

}

setup_piper() {
	package_install                            \
		piper    `# gaming mouse settings GUI` \

}

setup_rust() {
	package_install \
		rust \

}

setup_timeshift() {
	package_install                                \
		timeshift    `# backup and restore system` \

}

setup_torrential() {
	package_install                    \
		torrential    `torrent client` \

}

setup_unity() {
	package_install                 \
		unityhub    `# game engine` \

	POST_INSTALL+=("Change editors location")
}

setup_vim() {
	package_install                        \
		vim-plug    `# vim plugin manager` \

	cp .vimrc ~
}

setup_virtualbox() {
	# https://wiki.archlinux.org/title/VirtualBox

	package_install                  \
		virtualbox                   \
		virtualbox-host-modules-arch \
		virtualbox-ext-oracle        \

	sudo systemctl enable systemd-modules-load
	sudo systemctl start systemd-modules-load
	sudo modprobe vboxdrv
}

setup_vlc() {
	package_install                                                       \
		vlc-luajit    `# media player compatible with obs-studio-browser` \

}

setup_vscode() {
	package_install                                            \
		visual-studio-code-bin    `# proprietary vscode build` \

	POST_INSTALL+=("vscode: log in")
}

setup_wine() {
	package_install                                  \
		wine          `# compatibility layer`        \
		wine-gecko    `# internet explorer for wine` \
		wine-mono     `# .NET runtime for wine`      \
		winetricks    `# wine helper script`         \

	# WINEARCH=win32 WINEPREFIX=~/.win32/ winecfg
	# winetricks allfonts
	# winetricks settings fontsmooth=rgb
}

setup_wireshark() {
	package_install                                                       \
		wireshark-gtk2    `# network protocol analyzer with gtk frontend` \

	sudo usermod -a -G wireshark $USER
	POST_INSTALL+=("wireshark: reboot")
}

setup_wps_office() {
	package_install                             \
		wps-office       `# MS office but free` \
		ttf-wps-fonts    `# WPS office fonts`   \

}

setup_zoom() {
	package_install                          \
		zoom    `# gay video conference app` \

}

setup_zsh() {
	package_install \
		zsh \

	if [[ ! -d /home/pomp/.oh-my-zsh ]]; then
		# install oh my zsh
		sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

		# install powerlevel10k theme
		git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

		cp .zshrc ~
	else
		log "zsh already configured. Skipping."
	fi
}


# #################### [ ETC ] ####################

backup() {
	TIMESTAMP=$(date +%s)
	# backup dconf configuration
	dconf dump / > "$SCRIPT_DIR/dconf$TIMESTAMP.conf"

	# make a home directory backup
	rsync -a --info=progress2 --perms /home/pomp "$DATA_PATH/backup$TIMESTAMP"

	# create timeshift backup
	if ! command -v timeshift &> /dev/null; then
		error "failed to create timeshift backup. Timeshift command not found."
	else
		sudo timeshift --create --comments "auto created by developomp setup script ($TIMESTAMP)"
	fi
}

setup_local() {
	# setup for applications in second drive
	# add to application menu

	if [[ -d /media/pomp/data/programs/dnSpy-net-win32 ]]; then
		log "dnspy"
	fi

	if [[ -d /media/pomp/data/programs/tor-browser ]]; then
		log "tor browser"
	fi
}


# #################### [ TEST ] ####################
# Tests if script is ready to be executed

# check if script is running as root
if [[ ! $EUID -ne 0 ]]; then
	error "DO NOT RUN THIS SCRIPT AS ROOT"
	exit 1
fi

# check internet connection
if ! ping -c 1 archlinux.org &> /dev/null; then
	error "You are not connected to the internet"
fi


# #################### [ START ] ####################

# move to script directory (repo root)
cd "$SCRIPT_DIR" || {
	error "FAILED TO GO TO SCRIPT DIRECTORY"
	exit
}

# remove temporary files and folders that was not removed from previous run
rm -rf "./tmp"

echo
warn_no_label "NOTICE"
warn_no_label "  This is not a completely hands off process."
warn_no_label "  You need to monitor the process and take appropriate actions."
echo

read -p "Press (y) to continue. Press any other key to exit: " -n 1 -r
if [[ $REPLY =~ ^[^Yy]$ ]]; then
	echo
	exit
fi
echo


# #################### [ MAIN ] ####################

setup_essentials

options=(
	"4k_video_downloader"	""	off
	"backup"				""	off
	"blender"				""	off
	"brave"					""	off
	"cpu_undervolting"		""	off
	"discord"				""	off
	"dotnet"				""	off
	"fonts"					""	off
	"gimp"					""	off
	"gnome"					""	off
	"gnome_apps"			""	off
	"gnome_extensions"		""	off
	"go"					""	off
	"godot"					""	off
	"gsmartcontrol"			""	off
	"inkscape"				""	off
	"kdenlive"				""	off
	"keyboard"				""	off
	"obs"					""	off
	"osu"					""	off
	"middleclickpaste"		""	off
	"mystiq"				""	off
	"node"					""	off
	"pamac"					""	off
	"pavucontrol"			""	off
	"pip"					""	off
	"piper"					""	off
	"rust"					""	off
	"timeshift"				""	off
	"torrential"			""	off
	"unity"					""	off
	"vim"					""	off
	"virtualbox"			""	off
	"vlc"					""	off
	"vscode"				""	off
	"wine"					""	off
	"wireshark"				""	off
	"wps_office"			""	off
	"zoom"					""	off
	"zsh"					""	off
)

# choose from available options
cmd=(dialog --separate-output --checklist "Select Setup Operations to perform" 20 50 5) 
choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
clear
for choice in $choices; do
	case "$choice" in
		"4k_video_downloader")	setup_4kvideodownloader;;
		"blender")				setup_blender;;
		"brave")				setup_brave;;
		"backup")				backup;;
		"cpu_undervolting")		setup_cpu_undervolting;;
		"discord")				setup_discord;;
		"dotnet")				setup_dotnet;;
		"fonts")				setup_fonts;;
		"gimp")					setup_gimp;;
		"gnome")				setup_gnome;;
		"gnome_apps")			setup_gnome_apps;;
		"gnome_extensions")		setup_gnome_extensions;;
		"go")					setup_go;;
		"godot")				setup_godot;;
		"gsmartcontrol")		setup_gsmartcontrol;;
		"inkscape")				setup_inkscape;;
		"kdenlive")				setup_kdenlive;;
		"keyboard")				setup_keyboard;;
		"obs")					setup_obs;;
		"osu")					setup_osu;;
		"middleclickpaste")		setup_middleclickpaste;;
		"mystiq")				setup_mystiq;;
		"node")					setup_node;;
		"pamac")				setup_pamac;;
		"pavucontrol")			setup_pavucontrol;;
		"pip")					setup_pip;;
		"piper")				setup_piper;;
		"rust")					setup_rust;;
		"timeshift")			setup_timeshift;;
		"torrential")			setup_torrential;;
		"unity")				setup_unity;;
		"vim")					setup_vim;;
		"virtualbox")			setup_virtualbox;;
		"vlc")					setup_vlc;;
		"vscode")				setup_vscode;;
		"wine")					setup_wine;;
		"wireshark")			setup_wireshark;;
		"wps_office")			setup_wps_office;;
		"zoom")					setup_zoom;;
		"zsh")					setup_zsh;;
	esac
done


# #################### [ CLEANUP ] ####################

# remove temporary directory
rm -rf "$SCRIPT_DIR/tmp"


# #################### [ DONE ] ####################
# print some info after installation

title "DONE"

echo

# show what to do manually
if [ ! ${#POST_INSTALL[@]} -eq 0 ]; then
    log_no_label "now:"

	for doWhat in "${POST_INSTALL[@]}"; do
		log_no_label "  - $doWhat"
	done
fi
