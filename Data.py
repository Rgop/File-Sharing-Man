# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
text = f"<b>○ 👑 Creator : <a href='tg://user?id={OWNER_ID}'>RG</a>\n○ ⚜ Anime in Hindi: <a href='https://t.me/Dub_Anime_in_Hindi'>Join</a>\n○ ⚜ Anime Series: <a href='https://t.me/Anime_Series_in_Hindi_Dubbed'>Join</a>\n○ ⚜ Anime Movies: <a href='https://t.me/Dub_Anime_Movies_in_Hindi'>Join</a>\n○ ⚜ Hindi Official: <a href='https://t.me/Crunchyroll_Anime_Hindi_Official'>Join</a>\n○ ⚜ Any Problem: @RG_Anime_Group</b>",

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man v4</a>

👨‍💻 Develoved by </b><a href='https://t.me/Lunatic0de/101'>@Lunatic0de</a>
"""
