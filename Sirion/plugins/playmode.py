from config import BANNED_USERS
from strings import get_command
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup
from Sirion import app
from Sirion.utils.decorators import language
from Sirion.utils.inline.settings import playmode_users_markup
from Sirion.utils.database import get_playmode, get_playtype, is_nonadmin_chat


PLAYMODE_COMMAND = get_command("PLAYMODE_COMMAND")


@app.on_message(
    filters.command(PLAYMODE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def playmode_(client, message: Message, _):
    playmode = await get_playmode(message.chat.id)
    Direct = True if playmode == "Direct" else None

    is_non_admin = await is_nonadmin_chat(message.chat.id)
    Group = None if is_non_admin else True

    playty = await get_playtype(message.chat.id)
    Playtype = None if playty == "Everyone" else True
    buttons = playmode_users_markup(_, Direct, Group, Playtype)
    response = await message.reply_text(
        _["playmode_1"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
