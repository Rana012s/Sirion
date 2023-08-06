from config import BANNED_USERS
from strings import get_command

from pyrogram import filters
from pyrogram.types import Message

from Sirion import app
from Sirion.utils.decorators import AdminRightsCheck
from Sirion.utils.database.memorydatabase import set_loop

# Commands
LOOP_COMMAND = get_command("LOOP_COMMAND")


@app.on_message(
    filters.command(LOOP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(cli, message: Message, _, chat_id):
    if len(message.command) != 2:
        return await message.reply_text(_["admin_24"])
    state = message.text.split(None, 1)[1].strip()

    if state.isnumeric():
        state = int(state)
        if 1 <= state <= 10:
            await set_loop(chat_id, state)
            return await message.reply_text(_["admin_25"].format(message.from_user.first_name, state))
        else:
            return await message.reply_text(_["admin_26"])

    elif state.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(_["admin_25"].format(message.from_user.first_name, 10))

    elif state.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text(_["admin_27"])

    else:
        return await message.reply_text(_["admin_24"])
