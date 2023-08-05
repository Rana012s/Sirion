import time
from aiohttp import ClientSession
from Sirion.core.git import git
from Sirion.core.dir import dirr
from Sirion.core.bot import MusicBot
from Sirion.core.userbot import Userbot
from Sirion.misc import dbb, heroku, sudo
from Sirion.platforms import YouTubeAPI, SpotifyAPI, TeleAPI


boot = time.time()

HELPABLE = {}

dirr()

git()

dbb()

heroku()

sudo()


app = MusicBot()

userbot = Userbot()

YouTube = YouTubeAPI()

Spotify = SpotifyAPI()

Telegram = TeleAPI()

aiohttpsession = ClientSession()

BOT_ID = 0
BOT_MENTION = ""
BOT_NAME = ""
BOT_USERNAME = ""

