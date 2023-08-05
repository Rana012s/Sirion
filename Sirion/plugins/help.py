import re
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from Sirion import *
from config import *
from Sirion.utils.eqline import page_load
from Sirion import HELPABLE, BOT_MENTION, app as bot


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(_, query):
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    TEXT = f"""
**ʜᴇʏ ʙᴀʙʏ {query.from_user.mention} ɪ ᴀᴍ {BOT_MENTION}

ɪ ᴀᴍ ᴀ sᴜᴘᴇʀғᴀsᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ᴍᴀɴʏ ᴜsᴇғᴜʟ & ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs**
"""
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data="back"),
                    InlineKeyboardButton(text="• close •", callback_data="close")
                ]
            ]
        )
        await query.message.edit(
            text=text,
            reply_markup=key
        )
    elif prev_match:
        current_page = int(prev_match.group(1))
        buttons = page_load(current_page - 1, HELPABLE, "help")
        await query.message.edit(
            TEXT,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif next_match:
        current_page = int(next_match.group(1))
        buttons = page_load(current_page + 1, HELPABLE, "help")
        await query.message.edit(
            TEXT,
            reply_markup=InlineKeyboardMarkup(buttons)
        )


@bot.on_callback_query(filters.regex("close"))
async def close(_, query):
    await query.message.delete()


@bot.on_callback_query(filters.regex("home"))
async def home(_, query):
    buttons = BUTT
    TEXT = f"""
**ʜᴇʏ ʙᴀʙʏ {query.from_user.mention} ɪ ᴀᴍ {BOT_MENTION}

ɪ ᴀᴍ ᴀ sᴜᴘᴇʀғᴀsᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ᴍᴀɴʏ ᴜsᴇғᴜʟ & ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs**
"""
    await query.message.edit(
          TEXT,
          reply_markup=InlineKeyboardMarkup(buttons)
    )


@bot.on_callback_query(filters.regex("back"))
async def back(_, query):
    buttons = page_load(0, HELPABLE, "help")
    TEXT = f"""
**ʜᴇʏ ʙᴀʙʏ {query.from_user.mention} ɪ ᴀᴍ {BOT_MENTION}

ɪ ᴀᴍ ᴀ sᴜᴘᴇʀғᴀsᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ᴍᴀɴʏ ᴜsᴇғᴜʟ & ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs**
"""
    await query.message.edit(
          TEXT,
          reply_markup=InlineKeyboardMarkup(buttons)
    )


@bot.on_message(filters.command(["help"]))
async def help_cmd(c, m):
    TEXT = f"""
**ʜᴇʟʟᴏ {m.from_user.mention} ɪ ᴀᴍ {BOT_MENTION}**

**ɪ ᴀᴍ ᴀ sᴜᴘᴇʀғᴀsᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ᴍᴀɴʏ ᴜsᴇғᴜʟ & ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs**
"""
    key = InlineKeyboardMarkup(page_load(0, HELPABLE, "help"))
    await c.send_message(m.chat.id, TEXT, reply_markup=key)

