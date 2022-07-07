from src.util import flatpak_install, paru_install, copy_file, run
from src import log


name = "Discord"

PLUGINS = (
    134,  # https://betterdiscord.app/plugin/Avatar%20Hover
    60,  # https://betterdiscord.app/plugin/BadgesEverywhere
    119,  # https://betterdiscord.app/plugin/BetterCodeblocks
    62,  # https://betterdiscord.app/plugin/BetterNsfwTag
    63,  # https://betterdiscord.app/plugin/BetterSearchPage
    228,  # https://betterdiscord.app/plugin/CallTimeCounter
    64,  # https://betterdiscord.app/plugin/CharCounter
    67,  # https://betterdiscord.app/plugin/CompleteTimestamps
    176,  # https://betterdiscord.app/plugin/Copier
    68,  # https://betterdiscord.app/plugin/CopyRawMessage
    69,  # https://betterdiscord.app/plugin/CreationDate
    186,  # https://betterdiscord.app/plugin/DoNotTrack
    132,  # https://betterdiscord.app/plugin/EmoteReplacer
    245,  # https://betterdiscord.app/plugin/FreeEmojis
    81,  # https://betterdiscord.app/plugin/GoogleTranslateOption
    284,  # https://betterdiscord.app/plugin/GrammarCorrect
    220,  # https://betterdiscord.app/plugin/GuildProfile
    83,  # https://betterdiscord.app/plugin/ImageUtilities
    295,  # https://betterdiscord.app/plugin/InvisibleTyping
    84,  # https://betterdiscord.app/plugin/JoinedAtDate
    85,  # https://betterdiscord.app/plugin/LastMessageDate
    287,  # https://betterdiscord.app/plugin/Link-Profile-Picture
    11,  # https://betterdiscord.app/plugin/MemberCount
    29,  # https://betterdiscord.app/plugin/PermissionsViewer
    158,  # https://betterdiscord.app/plugin/PlatformIndicators
    93,  # https://betterdiscord.app/plugin/QuickMention
    94,  # https://betterdiscord.app/plugin/ReadAllNotificationsButton
    179,  # https://betterdiscord.app/plugin/RedditMentions
    97,  # https://betterdiscord.app/plugin/RevealAllSpoilersOption
    98,  # https://betterdiscord.app/plugin/SendLargeMessages
    159,  # https://betterdiscord.app/plugin/ShowAllActivities
    291,  # https://betterdiscord.app/plugin/ShowConnections
    103,  # https://betterdiscord.app/plugin/ShowHiddenChannels
    104,  # https://betterdiscord.app/plugin/SpellCheck
    162,  # https://betterdiscord.app/plugin/StaffTag
    8,  # https://betterdiscord.app/plugin/SuppressReplyMentions
    253,  # https://betterdiscord.app/plugin/Typing%20Users%20Avatars
    196,  # https://betterdiscord.app/plugin/TypingIndicator
    293,  # https://betterdiscord.app/plugin/UserDetails
)


def setup():
    """Discord and better discord"""

    flatpak_install("com.discordapp.Discord")
    paru_install("betterdiscordctl-git")

    for id in PLUGINS:
        url = f"https://betterdiscord.app/Download?id={id}"
        log.log(f"installing {url}")

        # assumes that plugins is located in "~/.var/app/com.discordapp.Discord/config/BetterDiscord/plugins" because I'm using flatpak
        run(
            f'wget --content-disposition --no-clobber -P ~/.var/app/com.discordapp.Discord/config/BetterDiscord/plugins "{url}"'
        )

    run("betterdiscordctl -i flatpak install")
