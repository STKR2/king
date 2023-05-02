import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
import re
import sys
from config import BANNED_USERS, MUSIC_BOT_NAME
from pyrogram import filters
import config
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)

@app.on_message(
    command(["المطور سند","المبرمج سند","سند"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(6174535740)
    name = usr.first_name
    user = await client.get_chat(6174535740)
    Bio = user.bio
    async for photo in client.iter_profile_photos(6174535740, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**معلومات الـمبرمج قـشـطه 🥷**
                    
⎈ ¦ 𝐍𝐚𝐦𝐞 :  [{usr.first_name}](https://t.me/{usr.username})

⎈ ¦ 𝐁𝐢𝐨 : {Bio}

⎈ ¦ 𝐔𝐬𝐞𝐫 : @{usr.username} 🥷

⎈ ¦ 𝐈𝐝 : 6174535740 🥷 """, 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],               
          ]              
       )              
    )
                       
                                 
                                           
                                                     
                                                               
                                                                         
                                                                                   

@app.on_message(
    command(["سيفي سند","سيفي ساند","سيفي المطور سند","سي في سند","سي في ساند"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(6174535740)
    name = usr.first_name
    user = await client.get_chat(6174535740)
    Bio = user.bio
    async for photo in client.iter_profile_photos(6174535740, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**سـيفي الـمبرمج قـشـطه 🥷**
                    
⎈ ¦ 𝐍𝐚𝐦𝐞 :  [{usr.first_name}](https://t.me/{usr.username})

⎈ ¦ 𝐁𝐢𝐨 : {Bio}

⎈ ¦ 𝐔𝐬𝐞𝐫 : @{usr.username} 🥷

⎈ ¦ 𝐈𝐝 : 6174535740 🥷

⎈ ¦ 𝐀𝐠𝐞 : 𝟐𝟑 🥷

⎈ ¦ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 : 𝐈𝐓𝐀𝐋𝐘 🥷""", 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],               
          ]              
       )              
    )