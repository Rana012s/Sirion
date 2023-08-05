import sys
import config
from pyrogram import Client
from Sirion.logging import LOGGER
from Sirion import BOT_NAME


assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        
    async def start(self):
        LOGGER(__name__).info(f"Getting Assistants Info")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("TeamSirion")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"**» {BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴏɴᴇ sᴛᴀʀᴛᴇᴅ :**\n\n❄ ɴᴀᴍᴇ : {self.one.name}\n✨ ɪᴅ : `{self.one.id}`\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{self.one.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group"
                )
                sys.exit()

        if config.STRING2:
            await self.two.start()
            try:
                await self.one.join_chat("TeamSirion")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = get_me.first_name + " " + get_me.last_name
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"**» {BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴡᴏ sᴛᴀʀᴛᴇᴅ :**\n\n❄ ɴᴀᴍᴇ : {self.two.name}\n✨ ɪᴅ : `{self.two.id}`\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{self.two.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group"
                )
                sys.exit()
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")
