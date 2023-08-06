from sys import exit
from config import API_ID, API_HASH, STRING1, STRING2, LOG_GROUP_ID
from pyrogram import Client
from Sirion.logging import LOGGER


class Userbot(Client):
    def __init__(self):
        super().__init__(
            api_id=API_ID,
            api_hash=API_HASH,
            no_updates=True,
        )
        
    async def start(self):
        LOGGER(__name__).info("Getting Assistants Info")
        
        if STRING1:
            one = Client(
                api_id=API_ID,
                api_hash=API_HASH,
                name=str(STRING1),
                no_updates=True,
            )
            await one.start()
            try:
                await one.join_chat("TeamSirion")
            except Exception as e:
                LOGGER(__name__).error(f"Failed to join chat with Assistant 1: {e}")
            try:
                get_me = await one.get_me()
                one.username = get_me.username
                one.id = get_me.id
                one.mention = get_me.mention
                LOGGER(__name__).info(f"Assistant 1 Started")
                await one.send_message(LOG_GROUP_ID, f"**» Assistant 1 Started:** {one.mention}")
            except Exception as e:
                LOGGER(__name__).error(f"Failed to start Assistant 1: {e}")
                exit()
        
        if STRING2:
            two = Client(
                api_id=API_ID,
                api_hash=API_HASH,
                name=str(STRING2),
                no_updates=True,
            )
            await two.start()
            try:
                await two.join_chat("TeamSirion")
            except Exception as e:
                LOGGER(__name__).error(f"Failed to join chat with Assistant 2: {e}")
            try:
                get_me = await two.get_me()
                two.username = get_me.username
                two.id = get_me.id
                two.mention = get_me.mention
                LOGGER(__name__).info(f"Assistant 2 Started")
                await two.send_message(LOG_GROUP_ID, f"**» Assistant 2 Started:** {two.mention}")
            except Exception as e:
                LOGGER(__name__).error(f"Failed to start Assistant 2: {e}")
                exit()


userbot = Userbot()

