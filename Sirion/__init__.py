import time
import config
from aiohttp import ClientSession
from config import HELPABLE, BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION
from Sirion.core.git import git
from Sirion.core.dir import dirr
from Sirion.misc import dbb, heroku, sudo
from Sirion.platforms import YouTubeAPI, SpotifyAPI, TeleAPI


boot = time.time()

dirr()

git()

dbb()

heroku()

sudo()


app = config.app

userbot = config.userbot

YouTube = YouTubeAPI()

Spotify = SpotifyAPI()

Telegram = TeleAPI()

aiohttpsession = ClientSession()


HELPABLE = HELPABLE

BOT_ID = BOT_ID

BOT_MENTION = BOT_MENTION

BOT_NAME = BOT_NAME

BOT_USERNAME = BOT_USERNAME

