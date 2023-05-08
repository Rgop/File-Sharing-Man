# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
⚜ Anime in Hindi: </b><a href='https://t.me/Dub_Anime_in_Hindi'>Join</a>

⚜ Anime Series Hindi: </b><a href='https://t.me/Anime_Series_in_Hindi_Dubbed'>Join</a>

⚜ Anime Movies Hindi: </b><a href='https://t.me/Dub_Anime_Movies_in_Hindi'>Join</a>

⚜ Crunchyroll Anime Hindi: </b><a href='https://t.me/Crunchyroll_Anime_Hindi_Official'>Join</a>

🙋 Any Problem: </b><a href='https://t.me/RG_Anime_Group'>HERE</a>
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("⛩ᴄʜᴀɴɴᴇʟ⛩", callback_data="help"),
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("⛩ᴄʜᴀɴɴᴇʟ⛩", callback_data="about"),
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>RG Anime Episode:

@{} is a Telegram Bot for storing posts or files that can be accessed via a special link.
 • Creator: @{}
 • Anime Group: <a href='https://t.me/RG_Anime_Group'>αηιмє gяσυρ</a>
👨‍💻 Develoved by </b><a href='https://t.me/RG_Anime_Group'>RG</a>
"""
