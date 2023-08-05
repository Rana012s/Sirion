from config import SUPPORT_HEHE
from Sirion import *
from pyrogram.types import InlineKeyboardButton


def start_pannel(BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="˹ʜᴇʟᴘ ᴍᴇɴᴜ˼", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton(text="⚙ sᴇᴛᴛɪɴɢs", callback_data="settings_helper"),
        ],
        ]
    return buttons

def private_panel(BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="˹ᴜᴘᴅᴀᴛᴇꜱ˼", url="https://t.me/TeamSirion"),
            InlineKeyboardButton(text="˹ꜱᴜᴘᴘᴏʀᴛ˼", url=f"https://t.me/{SUPPORT_HEHE}")
        ],
        [
            InlineKeyboardButton(text="˹ʜᴇʟᴘ ᴍᴇɴᴜ˼", callback_data="settings_back_helper"),
        ]
    ]
    return buttons
