from strings import get_command
from config import MUSIC_BOT_NAME, BANNED_USERS, adminlist

from pyrogram import filters
from pyrogram.types import Message

from Sirion import app
from Sirion.misc import SUDOERS, db
from Sirion.core.call import AltCall
from Sirion.utils import AdminRightsCheck
from Sirion.utils.inline.speed import speed_markup
from Sirion.utils.inline.play import close_keyboard
from Sirion.utils.decorators.language import languageCB
from Sirion.utils.database.memorydatabase import is_active_chat, is_nonadmin_chat


checker = []

SPEED_COMMAND = get_command("SPEED_COMMAND")


@app.on_message(
    filters.command(SPEED_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def playback(cli, message: Message, _, chat_id):
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["speed_7"])
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await message.reply_text(_["speed_7"])
    upl = speed_markup(_, chat_id)
    return await message.reply_text(_["speed_6"].format(MUSIC_BOT_NAME), reply_markup=upl)


@app.on_callback_query(filters.regex("SpeedUP") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat, speed = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_6"], show_alert=True)
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins:
                return await CallbackQuery.answer(_["admin_18"], show_alert=True)
            elif CallbackQuery.from_user.id not in admins:
                return await CallbackQuery.answer(_["admin_19"], show_alert=True)
    playing = db.get(chat_id)
    if not playing:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await CallbackQuery.answer(_["speed_7"], show_alert=True)
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await CallbackQuery.answer(_["speed_7"], show_alert=True)
    checkspeed = (playing[0]).get("speed")

    if checkspeed and (str(checkspeed) == str(speed)):
        if str(speed) == "1.0":
            speed = "ɴᴏʀᴍᴀʟ"
        return await CallbackQuery.answer(_["speed_1"].format(speed), show_alert=True)
    if chat_id in checker:
        return await CallbackQuery.answer(_["speed_2"], show_alert=True)
    else:
        checker.append(chat_id)
    mystic = await app.send_message(
        CallbackQuery.message.chat.id,
        text=_["speed_3"].format(CallbackQuery.from_user.mention),
        reply_markup=close_keyboard
    )
    try:
        await AltCall.speedup_stream(chat_id, file_path, speed, playing)
    except Exception as e:
        print(e)
        if chat_id in checker:
            checker.remove(chat_id)
        return await mystic.edit_text(_["speed_4"], reply_markup=close_keyboard)
    if chat_id in checker:
        checker.remove(chat_id)
    await mystic.edit_text(_["speed_5"].format(speed, CallbackQuery.from_user.mention), reply_markup=close_keyboard)
