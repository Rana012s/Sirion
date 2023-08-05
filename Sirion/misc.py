import time
import config
import socket
import heroku3

from pyrogram import filters
from Sirion.logging import LOGGER
from Sirion.core.mongo import pymongodb


SUDOERS = filters.user()

HAPP = None

_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Database Loaded.")


def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    sudoersdb = pymongodb.sudoers
    sudoers = sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    SUDOERS.add(OWNER)
    if OWNER not in sudoers:
        sudoers.append(OWNER)
        sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for x in sudoers:
            SUDOERS.add(x)
    LOGGER(__name__).info("Sudo Users Loaded Successfully.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info("Heroku App Configured Successfully.")
            except BaseException:
                LOGGER(__name__).warning(
                    "Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )
