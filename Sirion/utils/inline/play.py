import math
from config import SUPPORT_GROUP
from Sirion.utils.formatters import time_to_seconds
from Sirion import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    ax = math.floor(percentage)
    if 0 < ax <= 10:
        bar = "◉—————————"
    elif 10 < ax < 20:
        bar = "—◉————————"
    elif 20 <= ax < 30:
        bar = "——◉———————"
    elif 30 <= ax < 40:
        bar = "———◉——————"
    elif 40 <= ax < 50:
        bar = "————◉—————"
    elif 50 <= ax < 60:
        bar = "—————◉————"
    elif 60 <= ax < 70:
        bar = "——————◉———"
    elif 70 <= ax < 80:
        bar = "———————◉——"
    elif 80 <= ax < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"

    buttons = [
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer")
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="☆", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}")
        ],
        [
            InlineKeyboardButton(text="» sᴘᴇᴇᴅ »", callback_data=f"PanelMarkup {videoid}|{chat_id}"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")
        ]
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    ax = math.floor(percentage)
    if 0 < ax <= 10:
        bar = "◉—————————"
    elif 10 < ax < 20:
        bar = "—◉————————"
    elif 20 <= ax < 30:
        bar = "——◉———————"
    elif 30 <= ax < 40:
        bar = "———◉——————"
    elif 40 <= ax < 50:
        bar = "————◉—————"
    elif 50 <= ax < 60:
        bar = "—————◉————"
    elif 60 <= ax < 70:
        bar = "——————◉———"
    elif 70 <= ax < 80:
        bar = "———————◉——"
    elif 80 <= ax < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"

    buttons = [
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer")
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}")
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="☆", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}")
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")
        ],
    ]
    return buttons


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}")
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}")
        ]
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_3"], callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}")
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}")
        ]
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"JavaPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"JavaPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}")
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}")
        ]
    ]
    return buttons


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}")
        ],
        [
            InlineKeyboardButton(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}")
        ]
    ]
    return buttons


close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")
                ]    
            ]
        )


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
                InlineKeyboardButton(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5"),
                InlineKeyboardButton(text="ɴᴏʀᴍᴀʟ", callback_data=f"SpeedUP {chat_id}|1.0"),
                InlineKeyboardButton(text="🕓 0.75x", callback_data=f"SpeedUP {chat_id}|0.75")
            ],
            [
                InlineKeyboardButton(text="⟳ ᴇɴᴀʙʟᴇ ʟᴏᴏᴘ ⟲", callback_data=f"ADMIN Loop|{chat_id}")
            ], 
            [
                InlineKeyboardButton(text="🕤 1.5x", callback_data=f"SpeedUP {chat_id}|1.5"),
                InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data=f"MainMarkup {videoid}|{chat_id}"),
                InlineKeyboardButton(text="🕛 2.0x", callback_data=f"SpeedUP {chat_id}|2.0")
            ]
    ]
    return buttons
