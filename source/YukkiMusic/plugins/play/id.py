import asyncio
from YukkiMusic import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(
    command(["ايدي", "ايديي", "ا"])
    & ~filters.edited
)
async def elkatibk(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    username = f"@{message.from_user.username}"
    bio = (await app.get_chat(message.from_user.id)).bio
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text(       f"""◎ ¦ 𝐍𝐚𝐦𝐞 {message.from_user.mention}\n\n◎ ¦ 𝐔𝐬𝐞𝐫  @{message.from_user.username}\n\n◎ ¦ 𝐈𝐃 `{message.from_user.id}`\n\n◎ ¦ 𝐁𝐢𝐨 **{bio}**\n\n\n ◎ ¦ 𝐈𝐃 𝐆𝐑𝐎𝐔𝐏 '{message.chat.id}' """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       name, url=f"https://t.me/{message.from_user.username}")
                ],
                [  
                    InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝞝 ࿊ 𝙏𝙐𝙍𝘽𝙊", url=f"https://t.me/SOURCE_Turbo"),
                ],
            ]
        ),
    )
    

