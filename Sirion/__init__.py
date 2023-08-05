import time
from aiohttp import ClientSession
from config import HELPABLE, BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION
from Sirion.core.git import git
from Sirion.core.dir import dirr
from Sirion.core.bot import MusicBot
from Sirion.core.userbot import Userbot
from Sirion.misc import dbb, heroku, sudo
from Sirion.platforms import YouTubeAPI, SpotifyAPI, TeleAPI


boot = time.time()

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


HELPABLE = HELPABLE

BOT_ID = BOT_ID

BOT_MENTION = BOT_MENTION

BOT_NAME = BOT_NAME

BOT_USERNAME = BOT_USERNAME

