#!/bin/bash

# don't remove line after package_install
# it will result in this syntax error: unexpected end of file


# #################### [ ESSENTIALS ] ####################
# Installs essential packages and defining important functions

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
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
	paru -S --noconfirm "$@"
}

package_remove() {
	paru -R --noconfirm "$@"
}

install_paru() {
	log "installing paru"

	smart_mkdir "$SCRIPT_DIR/tmp"
	cd "$SCRIPT_DIR/tmp" || (error "failed to move to $SCRIPT_DIR/tmp for paru installation" && exit 1)
	sudo pacman --noconfirm -S --needed base-devel git
	git clone https://aur.archlinux.org/paru.git
	cd ./paru && makepkg -si

	cd "$SCRIPT_DIR" || (error "failed to come back to working directory after installing paru" && exit 1)
}

setup_essentials() {
	# install paru if it does not exist
	if ! command -v paru &> /dev/null; then
		install_paru
	fi

	package_install dialog &> /dev/null
	# enable multilib, color, parallel download, and total download in /etc/pacman.conf
}


# #################### [ DEFINING SETUP ] ####################
# Define instructions on how to setup applications & stuff

setup_4kvideodownloader() {
	package_install \
		4kvideodownloader \

}

setup_alacarte() {
	package_install \
		alacarte \

}

setup_blender() {
	package_install \
		blender \

}

setup_brave() {
	package_install \
		brave-beta-browser \

	# settings: DNS https cloudflare
	POST_INSTALL+=(
		"brave: sync device"
		"brave: restore onetab"
	)
}

setup_conky() {
	# enable on startup
	# copy conky files

	package_install \
		conky \
		vnstat    `# network traffic statistics` \

	sudo systemctl enable vnstat
	sudo systemctl start vnstat
}

setup_cpu_undervolting() {
	# Undervolting for intel CPU
	# https://wiki.archlinux.org/index.php/Undervolting_CPU

	package_install \
		intel-undervolt \

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

setup_cpupower_gui() {
	package_install \
		cpupower-gui \

}

setup_dconf() {
	:
	# must be done after install to make sure configs are not overwritten
	# dconf load / < $SCRIPT_DIR/dconf.conf
}

setup_deno() {
	package_install \
		deno \

}

setup_discord() {
	# assumes that plugins are located in ~/.config/BetterDiscord/plugins

	package_install \
		discord \
		betterdiscordctl-git \
		discord-overlay-git \

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

setup_dns() {
	:
	# https://1.1.1.1
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

	package_install \
		noto-fonts-emoji \
		nerd-fonts-noto-sans-mono    `# Terminal font` \

}

setup_dotnet() {
	package_install \
		dotnet-sdk \

}

setup_gimp() {
	package_install \
		gimp \

}

setup_gnome() {
	package_install \
		baobab                             `# Disk usage analysis` \
		dconf-editor                       `# GUI for dconf` \
		gnome-characters                   `# Search for emojis, special characters, and symbols` \
		gnome-clocks                       `# For multiple clocks for different time zones` \
		gnome-font-viewer                  `# Managing fonts` \
		gnome-logs                         `# GUI for system journal` \
		gnome-usage                        `# System resource statistics` \
		gnome-terminal-transparency        `# Transparent gnome terminal` \
		gnome-shell-extension-installer    `# Installation of gnome extensions from command line` \

	# install gnome extensions
	log "installing gnome extensions"
	extension_ids=(
		36      # lock-keys
		131     # touchpad-indicator
		355     # status-area-horizontal-spacing
		800     # remove-dropdown-arrows
		841     # freon
		906     # sound-output-device-chooser
		2741    # remove-alttab-delay-v2
		4000    # babar
	)

	for extension_id in "${extension_ids[@]}"; do
		log "- https://extensions.gnome.org/extension/$extension_id"
		gnome-shell-extension-installer --yes $extension_id
	done

	log "Restarting gnome shell"
	killall -3 gnome-shell

	POST_INSTALL+=("gnome: enable gnome extensions")
}

setup_gpick() {
	package_install \
		gpick \

}

setup_go() {
	package_install \
		go \

}

setup_godot() {
	package_install \
		godot \

}

setup_graphics() {
	# https://wiki.manjaro.org/index.php/Configure_Graphics_Cards#Automated_Identification_and_Installation
	sudo mhwd -a pci nonfree 0300

	# /etc/X11/Xwrapper.config write:
	# allowed_users=anybody
	# needs_root_rights=yes

	# sudo chmod u+s /usr/lib/Xorg.wrap
	POST_INSTALL+=("Graphics: Reboot")
}

setup_gsmartcontrol() {
	package_install \
		gsmartcontrol \

}

setup_hardinfo() {
	package_install \
		hardinfo \

}

setup_inkscape() {
	package_install \
		inkscape \

}

setup_java() {
	package_install \
		jdk                                `# oracle java development kit` \
		jdk8                               `# ` \

}

setup_kdenlive() {
	package_install \
		kdenlive-appimage \

}

setup_keyboard() {
	package_install \
		ibus-hangul \

	POST_INSTALL+=("keyboard: setup korean keyboard and reboot")
}

setup_local() {
	# setup for applications in second drive
	# add to application menu
	# office 2019 wine

	if [[ -d /media/pomp/data/programs/dnSpy-net-win32 ]]; then
		log "dnspy"
	fi

	if [[ -d /media/pomp/data/programs/tor-browser ]]; then
		log "tor"
	fi
}

setup_middleclickpaste() {
	:
	# make it autostart
}

setup_mystiq() {
	package_install \
		mystiq \

}

setup_node() {
	package_install \
		nodejs                             `# Javascript on servers!` \
        yarn                               `# better node package manager` \
		deno                               `# node++ or smth` \

	# https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
	# export PATH="$(yarn global bin):$PATH"
}

setup_obs() {
	package_install \
		obs-plugin-input-overlay-bin    `# show inputs in OBS` \
		obs-studio-browser              `# screen recording and streaming` \

}

setup_optimus_manager() {
	# Not using power switching
	# read this wiki[^1] about power management with acpi call for more information
	# [^1]: https://github.com/Askannz/optimus-manager/wiki/A-guide--to-power-management-options#configuration-4--acpi_call

	package_install \
		gwe                   `# nvidia GPU overclocking https://gitlab.com/leinardi/gwe` \
		optimus-manager       `# https://github.com/Askannz/optimus-manager` \
		optimus-manager-qt    `# https://github.com/Shatur/optimus-manager-qt` \
		gdm-prime             `# ` \

	# launch on startup
	# nvidia as default

	# Performance: 265, 750
	# Energy Saver: -155, -365
}

setup_osu() {
	package_install \
		osu \

}

setup_pavucontrol() {
	package_install \
		pavucontrol \

}

setup_pip() {
	package_install \
		python-pip \

}

setup_piper() {
	package_install \
		piper \

}

setup_rust() {
	package_install \
		rust \

}

setup_shfmt() {
	:
}

setup_timeshift() {
	package_install \
		timeshift \

}

setup_torrential() {
	package_install \
		torrential \

}

setup_unity() {
	package_install \
		unityhub \

	POST_INSTALL+=("Setup vscode for Unity")
	POST_INSTALL+=("Change editor location")
}

setup_user_directories() {
	:
	# edit ~/.config/user-dirs.dirs:

	# XDG_DESKTOP_DIR="$HOME/Desktop"
	# XDG_DOWNLOAD_DIR="/media/pomp/data/Downloads"
	# XDG_TEMPLATES_DIR="$HOME/Templates"
	# XDG_PUBLICSHARE_DIR="$HOME/Public"
	# XDG_DOCUMENTS_DIR="/media/pomp/data/Documents"
	# XDG_MUSIC_DIR="/media/pomp/data/Music"
	# XDG_PICTURES_DIR="/media/pomp/data/Pictures"
	# XDG_VIDEOS_DIR="/media/pomp/data/Videos"
}

setup_virtualbox() {
	# https://wiki.manjaro.org/index.php/VirtualBox

	package_install \
		virtualbox \
		linux510-virtualbox-host-modules \
		virtualbox-ext-oracle \

	sudo vboxreload
}

setup_vscode() {
	package_install \
		visual-studio-code-bin \

	POST_INSTALL+=("vscode: log in")
}

setup_vim() {
	package_install \
		vim \

}

setup_vlc() {
	package_install \
		vlc \

}

setup_wine() {
	package_install \
		wine \
		wine-gecko \
		wine-mono \
		winetricks \

	# - `WINEARCH=win32 WINEPREFIX=~/.win32/ winecfg`
	# - `winetricks allfonts`
	# - `winetricks settings fontsmooth=rgb`
}

setup_wireshark() {
	package_install \
		wireshark-gtk2 \

	sudo usermod -a -G wireshark $USER
	POST_INSTALL+=("wireshark: reboot")
}

setup_wps_office() {
	package_install \
		wps-office \
		ttf-wps-fonts \

}

setup_zoom() {
	package_install \
		zoom \

}


# #################### [ INSTALL ] ####################

backup() {
	dconf dump / > "$SCRIPT_DIR/dconf.conf"
	# copy /home/pomp directory
	# timeshift settings
	sudo timeshift --create --comments "auto created by developomp setup script"
}

install_arch() {
	:
	# check if drives exist
	# if $RESET$BOLD/media/pomp/data$GREEN exists in fstab and is mounted
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

cd "$SCRIPT_DIR" || {
	error "FAILED TO FIND SCRIPT DIRECTORY"
	exit
}

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

cmd=(dialog --separate-output --checklist "Select Setup Operations to perform" 20 50 5) 

options=(
	"remove_unnecessary_packages"  ""  off
	"4k_video_downloader"          ""  off
	"blender"                      ""  off
	"brave"                        ""  off
	"deno"                         ""  off
	"discord"                      ""  off
	"dotnet"                       ""  off
	"fonts"                        ""  off
	"gimp"                         ""  off
	"gnome"                        ""  off
	"go"                           ""  off
	"godot"                        ""  off
	"graphics"                     ""  off
	"gsmartcontrol"                ""  off
	"inkscape"                     ""  off
	"kdenlive"                     ""  off
	"keyboard"                     ""  off
	"obs"                          ""  off
	"osu"                          ""  off
	"piper"                        ""  off
	"rust"                         ""  off
	"torrential"                   ""  off
	"unity"                        ""  off
	"vim"                          ""  off
	"virtualbox"                   ""  off
	"vlc"                          ""  off
	"vscode"                       ""  off
	"wireshark"                    ""  off
	"wps_office"                   ""  off
	"zoom"                         ""  off
)

choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
clear
for choice in $choices; do
	case "$choice" in
		"4k_video_downloader")
			setup_4kvideodownloader;;
		"brave")
			setup_brave;;
		"blender")
			setup_blender;;
		"deno")
			setup_deno;;
		"discord")
			setup_discord;;
		"dotnet")
			setup_dotnet;;
		"fonts")
			setup_fonts;;
		"gimp")
			setup_gimp;;
		"gnome")
			setup_gnome;;
		"go")
			setup_go;;
		"godot")
			setup_godot;;
		"gsmartcontrol")
			setup_gsmartcontrol;;
		"inkscape")
			setup_inkscape;;
		"kdenlive")
			setup_kdenlive;;
		"keyboard")
			setup_keyboard;;
		"obs")
			setup_obs;;
		"osu")
			setup_osu;;
		"piper")
			setup_piper;;
		"rust")
			setup_rust;;
		"torrential")
			setup_torrential;;
		"unity")
			setup_unity;;
		"vim")
			setup_vim;;
		"virtualbox")
			setup_virtualbox;;
		"vlc")
			setup_vlc;;
		"vscode")
			setup_vscode;;
		"wireshark")
			setup_wireshark;;
		"wps_office")
			setup_wps_office;;
		"zoom")
			setup_zoom;;
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

exit 0
