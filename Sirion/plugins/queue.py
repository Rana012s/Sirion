import asyncio
from config import (
    BANNED_USERS, TELEGRAM_AUDIO_URL,
    TELEGRAM_VIDEO_URL, STREAM_IMG_URL
)
from Sirion import BOT_MENTION as MUSIC_BOT_NAME
from strings import get_command
from pyrogram import filters
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message
from Sirion import app, YouTube
from Sirion.misc import db
from Sirion.utils.thumbnails import gen_thumb
from Sirion.utils import Altbin, get_channeplayCB
from Sirion.utils.formatters import seconds_to_min
from Sirion.utils.database import get_cmode, is_active_chat
from Sirion.utils.inline import queue_back_markup, queue_markup
from Sirion.utils.decorators.language import language, languageCB


QUEUE_COMMAND = get_command("QUEUE_COMMAND")
basic = {}


def get_duration(playing):
    file_path = playing[0]["file"]
    if "index_" in file_path or "live_" in file_path:
        return "ᴜɴᴋɴᴏᴡɴ"
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return "ᴜɴᴋɴᴏᴡɴ"
    else:
        return seconds_to_min(duration_seconds)


@app.on_message(filters.command(QUEUE_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def queue_com(client, message: Message, _):
    if message.command[0][0] == "c":
        chat_id = await get_cmode(message.chat.id)
        if chat_id is None:
            return await message.reply_text(_["setting_12"])
        try:
            await app.get_chat(chat_id)
        except:
            return await message.reply_text(_["cplay_4"])
        cplay = True
    else:
        chat_id = message.chat.id
        cplay = False
    if not await is_active_chat(chat_id):
        return await message.reply_text(_["general_6"])
    got = db.get(chat_id)
    if not got:
        return await message.reply_text(_["queue_2"])
    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    DUR = get_duration(got)

    if ("live_" in file) or ("vid_" in file):
        IMAGE = await gen_thumb(videoid)
    elif "index_" in file:
        IMAGE = STREAM_IMG_URL
    else:
        if videoid == "telegram":
            IMAGE = TELEGRAM_AUDIO_URL if typo == "Audio" else TELEGRAM_VIDEO_URL
        else:
            IMAGE = await gen_thumb(videoid)

    cap = f"""**{MUSIC_BOT_NAME} ᴩʟᴀʏᴇʀ**

✨ **ᴛɪᴛʟᴇ:** {title[:27]}
⌛️ **ᴅᴜʀᴀᴛɪᴏɴ:** {DUR}

🥀**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {user}

ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴡʜᴏʟᴇ ǫᴜᴇᴜᴇᴅ ʟɪsᴛ."""
    upl = queue_markup(_, "c" if cplay else "g", videoid)
    basic[videoid] = True
    await message.reply_photo(photo=IMAGE, caption=cap, reply_markup=upl)


@app.on_callback_query(filters.regex("GetTimer") & ~BANNED_USERS)
async def quite_timer(client, CallbackQuery: CallbackQuery):
    try:
        await CallbackQuery.answer()
    except:
        pass


@app.on_callback_query(filters.regex("GetQueued") & ~BANNED_USERS)
@languageCB
async def queued_tracks(client, CallbackQuery: CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, videoid = callback_request.split("|")
    try:
        chat_id, channel = await get_channeplayCB(_, what, CallbackQuery)
    except:
        return
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_6"], show_alert=True)
    got = db.get(chat_id)
    if not got:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    if len(got) == 1:
        return await CallbackQuery.answer(_["queue_5"], show_alert=True)
    await CallbackQuery.answer()
    basic[videoid] = False
    buttons = queue_back_markup(_, what)
    thumbnail = await YouTube.thumbnail(videoid, True)
    med = InputMediaPhoto(media=thumbnail, caption=_["queue_1"])
    await CallbackQuery.edit_message_media(media=med)
    j = 0
    msg = ""
    for x in got:
        j += 1
        if j == 1:
            msg += _["queue_7"].format(MUSIC_BOT_NAME, x["title"], x["dur"], x["by"])
        elif j == 2:
            msg += _["queue_8"].format(x["title"], x["dur"], x["by"])
        else:
            msg += _["queue_9"].format(x["title"], x["dur"], x["by"])

    if "Queued" in msg:
        if len(msg) < 700:
            await asyncio.sleep(1)
            return await CallbackQuery.edit_message_text(msg, reply_markup=buttons)
        if "✨" in msg:
            msg = msg.replace("✨", "")
        link = await Altbin(msg)
        if not link:
            return await CallbackQuery.message.reply_text(_["queue_6"])
        med = InputMediaPhoto(media=link, caption=_["queue_3"].format(link))
        await CallbackQuery.edit_message_media(media=med, reply_markup=buttons)
    else:
        await asyncio.sleep(1)
        return await CallbackQuery.edit_message_text(msg, reply_markup=buttons)


@app.on_callback_query(filters.regex("queue_back_timer") & ~BANNED_USERS)
@languageCB
async def queue_back(client, CallbackQuery: CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cplay = callback_data.split(None, 1)[1]
    try:
        chat_id, channel = await get_channeplayCB(_, cplay, CallbackQuery)
    except:
        return
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_6"], show_alert=True)
    got = db.get(chat_id)
    if not got:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    await CallbackQuery.answer(_["set_cb_8"], show_alert=True)

    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    DUR = get_duration(got)
    if ("live_" in file) or ("vid_" in file):
        IMAGE = await gen_thumb(videoid)
    elif "index_" in file:
        IMAGE = STREAM_IMG_URL
    else:
        if videoid == "telegram":
            IMAGE = (
                TELEGRAM_AUDIO_URL
                if typo == "Audio"
                else TELEGRAM_VIDEO_URL
            )
        else:
            IMAGE = await gen_thumb(videoid)

    cap = f"""**{MUSIC_BOT_NAME} ᴩʟᴀʏᴇʀ**

✨ **ᴛɪᴛʟᴇ:** {title[:27]}
⌛️ **ᴅᴜʀᴀᴛɪᴏɴ:** {DUR}

🥀**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {user}

ᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴡʜᴏʟᴇ ǫᴜᴇᴜᴇᴅ ʟɪsᴛ."""
    upl = queue_markup(_, cplay, videoid)
    basic[videoid] = True
    med = InputMediaPhoto(media=IMAGE, caption=cap)
    await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
