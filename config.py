import re
import sys

from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "25981592"))
API_HASH = getenv("API_HASH", "709f3c9d34d83873d3c7e76cdd75b866")

BOT_TOKEN = getenv("BOT_TOKEN", "5932137530:AAHNrQMSeAuCGWqHfUa5kD4wl4DfVYK-nr4")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://shyxdoll13:shyxdoll@cluster0.nyyxhzb.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001954218150"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Menzy Music")

OWNER_ID = int(getenv("OWNER_ID", "5518687442"))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheRiruru/Sirion")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", "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" )

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TheAltron")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/AltronChats")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "54000"))

SET_CMDS = getenv("SET_CMDS", False)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/TheRiruru/Sirion")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "04bd2cf9ebad4b6cb54b0e24a039b15e")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "ac02869b41964e349fcda21cd87a902c")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "10"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "AQApbUAYYw4glxrilDTaNl26Zs20iH7LsUwMnf6dQyjiplMArSnrdo93Mjl68kMM0r9jcNzHfwcDlw7z_ar0eT2y6539rsbV7OHhprU-jqMs-7JnnazuS7fnKEvyFj0oJTNYQvECrx8KoxMc0Kqu4tEalSNrj_hRHt6XwNaFqTRw7FbDRCjjraysi2oxbfosx4nVas07q3m6Y8WFBwYAF8ZAzQCgmdGUvyoeW904pZ7diBNVCaWozIUdnQv2GupyTmqiTUp296bKviwKCUiq88H13NQBh2MBpp0uNGCfmEN_Gp66T6zfncEHQv0w2AnEbTIpsa8frBeCbj8wUGhqoQYvAAAAAVd2kRUA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
DEV = 5518687442
LOG_FILE_NAME = "RiruruLogs.txt"

adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}
autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/938d91267eedec0f8da06.jpg")

PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")

STATS_IMG_URL = getenv("STATS_IMG_URL", "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg")

TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "https://te.legra.ph/file/6298d377ad3eb46711644.jpg")

TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "https://te.legra.ph/file/6298d377ad3eb46711644.jpg")

STREAM_IMG_URL = getenv("STREAM_IMG_URL", "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg")

SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg")

YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/6298d377ad3eb46711644.jpg")

SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg")

SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg")

SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg")


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print("[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://")
        sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "Sirion/assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print("[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://")
            sys.exit()

if STATS_IMG_URL:
    if STATS_IMG_URL != "Sirion/assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print("[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://")
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "Sirion/assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print("[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://")
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "Sirion/assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print("[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://")
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "Sirion/assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print("[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://")
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "Sirion/assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print("[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://")
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "Sirion/assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print("[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://")
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print("Please Do Not Use Fancy Font in Music Bot's Name!")
