from YukkiMusic.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from YukkiMusic.utils.database import is_muted, mute_on
from YukkiMusic.utils.database import is_muted, mute_off
from YukkiMusic.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False



@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.channel
    & ~filters.edited
)
@app.on_message(
    command(["سورس","السورس","يا سورس","سورس تيربو","تيربو"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7bf6287a35f79aa6d70be.jpg",
        caption=f"""⋖⊶◎⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝 𖧊 𝙏𝙐𝙍𝘽𝙊⌯⊶◎⊷⋗
        
𖧊 ¦ [𓌹 ↱ 𝘿ٓ𝙀ٓ𝙑ٰٰ 𝙆ٓ𝙎ٓ𝙃ٓ𝙏ٓ𝘼ّ𝙃ٰ 𝘽ٰٓ𝘼ٓ𝙎ٓ𝙃َٓ𝘼 ↲ 𓌺](t.me/DEV_KSHTAH)

𖧊 ¦ [Yᥱ᥉ Ꭵ ꪔ ᥉ᥲ️ꪀᥲ️ժ ( انا فين وانت فين )](t.me/DEV_SANAD)
      
𖧊 ¦ [𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𖧊 𝙏𝙐𝙍𝘽𝙊](t.me/HELP1_TURBO)       
                              
𖧊 ¦ [𝙎𝙊𝙐𝙍𝘾𝞝 𖧊 𝙏𝙐𝙍𝘽𝙊](t.me/SOURCE_TURBO)     
                          
⋖⊶◎⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝 𖧊 𝙏𝙐𝙍𝘽𝙊⌯⊶◎⊷⋗""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝞝 𖧊 𝙏𝙐𝙍𝘽𝙊", url=f"https://t.me/SOURCE_Turbo"),
                ],[
                    InlineKeyboardButton(
                        "Yᥱ᥉ Ꭵ ꪔ ᥉ᥲ️ꪀᥲ️ժ ( انا فين وانت فين )", url=f"https://t.me/DEV_SANAD"), 
                    InlineKeyboardButton(
                        "𓌹 ↱ 𝘿ٓ𝙀ٓ𝙑ٰٰ 𝙆ٓ𝙎ٓ𝙃ٓ𝙏ٓ𝘼ّ𝙃ٰ 𝘽ٰٓ𝘼ٓ𝙎ٓ𝙃َٓ𝘼 ↲ 𓌺", url=f"https://t.me/DEV_KSHTAH"),
                ],[
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/SILA_11bot?startgroup=true"),
            ]
        ]
         ),
     )
  
