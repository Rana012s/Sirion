from datetime import datetime
from strings import get_command
from pyrogram import filters
from pyrogram.types import Message
from Sirion import app
from Sirion.misc import SUDOERS
from Sirion.core.call import JavaCall
from Sirion.utils import bot_sys_stats
from Sirion.utils.decorators.language import language



__MODULE__ = "bot"
__HELP__ = """
/start - get start message

/help - get help commands menu

/ping - check ping of the bot
"""

PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(filters.command(PING_COMMAND) & SUDOERS)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_text(_["ping_1"])
    start = datetime.now()
    pytgping = await JavaCall.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    await response.edit_text(
        _["ping_2"].format(resp, UP, DISK, RAM, CPU, pytgping)
    )
