from strings import get_command
from pyrogram import filters
from pyrogram.types import Message
from Sirion import app
from Sirion.misc import SUDOERS
from Sirion.utils.decorators import language
from Sirion.utils.database.memorydatabase import get_active_chats, get_active_video_chats

__MODULE__ = "active"
__HELP__ = """
/activevoice : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ᴛʜᴇ ʙᴏᴛ.

/activevideo : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs ᴏɴ ᴛʜᴇ ʙᴏᴛ.

/activechats : ɢᴇᴛ ꜱᴛᴀᴛꜱ ᴏꜰ ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛꜱ.

/autoend [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ] : ᴇɴᴀʙʟᴇ sᴛʀᴇᴀᴍ ᴀᴜᴛᴏ ᴇɴᴅ ɪғ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ
"""

ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")
FAST_AC = get_command("FAST_AC")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
@language
async def activevc(client, message: Message, _):
    mystic = await message.reply_text(_["active_2"])
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = _["S_B_9"]
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if text:
        await mystic.edit_text(_["active_4"].format(text), disable_web_page_preview=True)
    else:
        await mystic.edit_text(_["active_6"])


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND)  & SUDOERS)
@language
async def activevi_(client, message: Message, _):
    mystic = await message.reply_text(_["active_3"])
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = _["S_B_9"]
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if text:
        await mystic.edit_text(_["active_5"].format(text), disable_web_page_preview=True)
    else:
        await mystic.edit_text(_["active_7"])


@app.on_message(filters.command(FAST_AC) & SUDOERS)
@language
async def littleac(client, message: Message, _):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(_["active_1"].format(ac_audio, ac_video), quote=True)
