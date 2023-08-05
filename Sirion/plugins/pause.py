from config import BANNED_USERS
from strings import get_command

from pyrogram import filters
from pyrogram.types import Message

from Sirion import app
from Sirion.core.call import AltCall
from Sirion.utils.inline.play import close_keyboard
from Sirion.utils.decorators import AdminRightsCheck
from Sirion.utils.database import is_music_playing, music_off

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(filters.command(PAUSE_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])

    await music_off(chat_id)
    await AltCall.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )