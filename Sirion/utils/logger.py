from config import LOG, LOG_GROUP_ID
from Sirion import app, BOT_MENTION
from Sirion.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.id != LOG_GROUP_ID:
            if message.chat.username:
                chatusername = f"@{message.chat.username}"
            else:
                chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
            logger_text = f"""**{BOT_MENTION} ᴩʟᴀʏ ʟᴏɢɢᴇʀ**

**ᴄʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
**ᴜsᴇʀ:** {message.from_user.mention}
**ᴜsᴇʀɴᴀᴍᴇ:** @{message.from_user.username}
**ɪᴅ:** `{message.from_user.id}`
**ᴄʜᴀᴛ ʟɪɴᴋ:** {chatusername}

**sᴇᴀʀᴄʜᴇᴅ ғᴏʀ:** {message.text}
"""
            try:
                await app.send_message(LOG_GROUP_ID, text=logger_text, disable_web_page_preview=True)
            except:
                pass
        return
