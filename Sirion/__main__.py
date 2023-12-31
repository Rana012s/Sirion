import config
import asyncio
import importlib
from os import mkdir, path
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from Sirion.logging import LOGGER
from Sirion.core.userbot import userbot
from Sirion import app, HELPABLE, BOT_ID, BOT_NAME, BOT_MENTION, BOT_USERNAME
from Sirion.core.call import JavaCall
from Sirion.plugins import ALL_MODULES


loop = asyncio.get_event_loop()


async def init():
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION
    
    if not path.exists("/files/"):
        mkdir("/files/")
    if (
        not config.STRING1
        and not config.STRING2
    ):
        LOGGER("Sirion").error("Atleast Add A Pyrogram V2 String ...")
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Sirion").warning("Fill SPOTIFY_CLIENT_ID & SPOTIFY_CLIENT_SECRET To Play Music From SPOTIFY")
    
    await app.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_MENTION = getme.mention    
    BOT_NAME = getme.first_name + (getme.last_name or "")
    BOT_USERNAME = getme.username
    try:
        await app.send_message(config.LOG_GROUP_ID, f"**» ʙᴏᴛ sᴛᴀʀᴛᴇᴅ** : {BOT_MENTION}")
    except:
        pass

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module("Sirion.plugins." + all_module)
        if (hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__):
            imported_module.__MODULE__ = imported_module.__MODULE__
            
            if (hasattr(imported_module, "__HELP__") and imported_module.__HELP__):
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
                
        print(f"Imported: {all_module}.py")
    LOGGER("Sirion.plugins").info("Necessary Modules Imported Successfully.")
    
    await userbot.start()
    await JavaCall.start()
    try:
        await JavaCall.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Sirion").error("[ERROR] - \n\nPlease turn on your Logger Group's Voice Call")
    except:
        pass
        
    await JavaCall.decorators()
    LOGGER("Sirion").info("Sirion Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Sirion").info("Stopping Music Bot ...")
