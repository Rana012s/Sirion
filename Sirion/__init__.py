import time
from aiohttp import ClientSession
from config import HELPABLE, BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION
from Sirion.core.bot import app
from Sirion.core.call import JavaCall
from Sirion.core.userbot import userbot
from Sirion.core.git import git
from Sirion.core.dir import dirr
from Sirion.misc import dbb, heroku, sudo


boot = time.time()

dirr()

git()

dbb()

heroku()

sudo()


app = app

userbot = userbot

JavaCall = JavaCall


aiohttpsession = ClientSession()

HELPABLE = HELPABLE

BOT_ID = BOT_ID

BOT_MENTION = BOT_MENTION

BOT_NAME = BOT_NAME

BOT_USERNAME = BOT_USERNAME

