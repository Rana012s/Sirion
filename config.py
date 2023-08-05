import re
import os
import sys
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from Sirion.core.bot import MusicBot
from Sirion.core.userbot import Userbot


if os.path.exists("sample.env"):
    load_dotenv("sample.env")
    

API_ID = int(getenv("API_ID"))

API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB = getenv("MONGO_DB")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))

OWNER_ID = int(getenv("OWNER_ID", "5180447182"))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ExoticHero/Sirion")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TeamSirion")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/TheDarFrekerz")

app = MusicBot()

userbot = Userbot()

HELPABLE = {}

LOAD = []

NO_LOAD = []

BOT_ID = 0

BOT_MENTION = ""

BOT_NAME = ""

BOT_USERNAME = ""

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "54000"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "04bd2cf9ebad4b6cb54b0e24a039b15e")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "ac02869b41964e349fcda21cd87a902c")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "10"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))


STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2

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
