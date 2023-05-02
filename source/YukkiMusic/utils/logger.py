#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
⋖⊶◎⊷⌯[𝙎𝙊𝙐𝙍𝘾𝞝 ࿊ 𝙏𝙐𝙍𝘽𝙊](https://t.me/SOURCE_TURBO)⌯⊶◎⊷⋗

**نـيم الـجروب :** {message.chat.title} [`{message.chat.id}`]

**البني أدم الي شـغل :** {message.from_user.mention}

**يـوزر البني أدم :** @{message.from_user.username}
**ايـدي البني أدم :** `{message.from_user.id}`

**لـنك الـجروب :** {chatusername}
**اللـمطلوب :** {message.text}
**اشـتغل من :** {streamtype}

⋖⊶◎⊷⌯[𝙎𝙊𝙐𝙍𝘾𝞝 ࿊ 𝙏𝙐𝙍𝘽𝙊](https://t.me/SOURCE_TURBO)⌯⊶◎⊷⋗"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
