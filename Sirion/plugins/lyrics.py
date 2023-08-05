import re

from os import remove
from lyricsgenius import Genius

from config import BANNED_USERS
from strings import get_command

from pyrogram import filters
from pyrogram.types import Message

from Sirion import app
from Sirion.utils.decorators.language import language


###Commands
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

y = Genius(
    "C7mS2YT19wBFGem83Bf12Y9Rg28I6EtuZhWLoAWfOODAzJXwS_44f56H-QWVzeKn",
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False


@app.on_message(filters.command(LYRICS_COMMAND) & ~filters.edited & ~BANNED_USERS)
@language
async def lrsearch(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text(_["lyrics_1"])
    title = message.text.split(None, 1)[1]
    m = await message.reply_text(_["lyrics_2"])
    S = y.search_song(title, get_full_info=False)
    if S is None:
        return await m.edit_text(_["lyrics_3"].format(title), disable_web_page_preview=True)
    lyric = S.lyrics
    if "Embed" in lyric:
        lyric = re.sub(r"\d*Embed", "", lyric)
    ran_hash = f"\\files\JavaLyrics{message.chat.id}{message.from_user.id}.txt"
    with open(ran_hash, "w") as lyr:
        lyr.write(lyric)
    try:
        await message.reply_document(ran_hash, caption=_["lyrics_4"].format(title), file_name=ran_hash)
        await m.delete()
    except Exception as e:
        await m.edit_text(_["error_1"].format(str(e)))
    finally:
        remove(ran_hash)
