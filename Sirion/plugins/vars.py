import asyncio
import config

from pyrogram import filters
from strings import get_command

from Sirion import app
from Sirion.misc import SUDOERS
from Sirion.utils.formatters import convert_bytes
from Sirion.utils.database.memorydatabase import get_video_limit

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text("ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ... ɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs...")
    v_limit = await get_video_limit()
    MUSIC_BOT_NAME = config.MUSIC_BOT_NAME
    up_r = f"[ʀᴇᴩᴏ]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "ʏᴇs"
    else:
        ass = "ɴᴏ"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "ʏᴇs"
    else:
        pvt = "ɴᴏ"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "ʏᴇs"
    else:
        down = "ɴᴏ"

    if not config.GITHUB_REPO:
        git = "ɴᴏ"
    else:
        git = f"[ʀᴇᴩᴏ]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "ɴᴏ"
    else:
        start = f"[ɪᴍᴀɢᴇ]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "ɴᴏ"
    else:
        s_c = f"[ᴄʜᴀɴɴᴇʟ]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "ɴᴏ"
    else:
        s_g = f"[sᴜᴩᴩᴏʀᴛ]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "ɴᴏ"
    else:
        token = "ʏᴇs"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "ɴᴏ"
    else:
        sotify = "ʏᴇs"
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**ᴍᴜsɪᴄ ʙᴏᴛ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs:**

**<u>ʙᴀsɪᴄ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴍᴜsɪᴄ_ʙᴏᴛ_ɴᴀᴍᴇ** : `{MUSIC_BOT_NAME}`
**ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** : `{play_duration} ᴍɪɴᴜᴛᴇs`
**sᴏɴɢ_ᴅᴏᴡɴʟᴏᴀᴅ_ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** :` {song} ᴍɪɴᴜᴛᴇs`
**ᴏᴡɴᴇʀ_ɪᴅ** : `{config.OWNER_ID}`
    
**<u>ʀᴇᴩᴏsɪᴛᴏʀʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴜᴩsᴛʀᴇᴀᴍ_ʀᴇᴩᴏ** : {up_r}
**ᴜᴩsᴛʀᴇᴀᴍ_ʙʀᴀɴᴄʜ** : `{up_b}`
**ɢɪᴛʜᴜʙ_ʀᴇᴩᴏ** : {git}
**ɢɪᴛ_ᴛᴏᴋᴇɴ**: `{token}`


**<u>ʙᴏᴛ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴀᴜᴛᴏ_ʟᴇᴀᴠɪɴɢ_ᴀssɪsᴛᴀɴᴛ** : `{ass}`
**ᴀssɪsᴛᴀɴᴛ_ʟᴇᴀᴠᴇ_ᴛɪᴍᴇ** : `{auto_leave} sᴇᴄᴏɴᴅs`
**ᴀᴜᴛᴏ_ᴅᴏᴡɴʟᴏᴀᴅs_ᴄʟᴇᴀʀ** : `{down}`
**ᴩʀɪᴠᴀᴛᴇ_ʙᴏᴛ_ᴍᴏᴅᴇ** : `{pvt}`
**ʏᴏᴜᴛᴜʙᴇ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** : `{yt_sleep} sᴇᴄᴏɴᴅs`
**ᴛᴇʟᴇɢʀᴀᴍ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** :` {tg_sleep} sᴇᴄᴏɴᴅs`
**ᴄʟᴇᴀɴᴍᴏᴅᴇ_ᴍɪɴs** : `{cm} ᴍɪɴᴜᴛᴇs`
**ᴠɪᴅᴇᴏ_sᴛʀᴇᴀᴍ_ʟɪᴍɪᴛ** : `{v_limit} ᴄʜᴀᴛs`
**sᴇʀᴠᴇʀ_ᴩʟᴀʏʟɪsᴛ_ʟɪᴍɪᴛ** :` {playlist_limit}`
**ᴩʟᴀʏʟɪsᴛ_ғᴇᴛᴄʜ_ʟɪᴍɪᴛ** :` {fetch_playlist}`

**<u>sᴩᴏᴛɪғʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_ɪᴅ** :` {sotify}`
**sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_sᴇᴄʀᴇᴛ** : `{sotify}`

**<u>ᴘʟᴀʏꜱɪᴢᴇ ᴠᴀʀꜱ:</u>**
**ᴛɢ_ᴀᴜᴅɪᴏ_ғʟɪᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_aud}`
**ᴛɢ_ᴠɪᴅᴇᴏ_ғɪʟᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_vid}`

**<u>ᴇxᴛʀᴀ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴜᴘᴅᴀᴛᴇꜱ_ᴄʜᴀɴɴᴇʟ** :  {s_c}
**sᴜᴩᴩᴏʀᴛ_ɢʀᴏᴜᴩ** :  {s_g}
**sᴛᴀʀᴛ_ɪᴍɢ_ᴜʀʟ** :  {start}"""
    await asyncio.sleep(1)
    await mystic.edit_text(text, disable_web_page_preview=True)
