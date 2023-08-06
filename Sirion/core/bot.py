import sys
from config import API_ID, API_HASH, BOT_TOKEN, LOG_GROUP_ID
from Sirion import BOT_MENTION
from pyrogram import Client
from Sirion.logging import LOGGER


class MusicBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "Sirion",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.id = get_me.id
        a = await self.get_chat_member(LOG_GROUP_ID, self.id)
        
        try:
            LOGGER(__name__).info(f"MusicBot Started as {self.name}")
            await self.send_message(
                LOG_GROUP_ID, f"**» {BOT_MENTION} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ**"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group"
            )
            sys.exit()


app = MusicBot()
