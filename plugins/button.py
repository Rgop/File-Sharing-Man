# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ sᴇʀɪᴇs ⛩", url=f"https://t.me/Anime_Series_in_Hindi_Dubbed"),
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇs ⛩", url=f"https://t.me/Dub_Anime_Movies_in_Hindi"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇs ⛩", url=f"https://t.me/Dub_Anime_Movies_in_Hindi"),
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ sᴇʀɪᴇs ⛩", url=f"https://t.me/Anime_Series_in_Hindi_Dubbed"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ sᴇʀɪᴇs ⛩", url=f"https://t.me/Anime_Series_in_Hindi_Dubbed"),
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇs ⛩", url=f"https://t.me/Dub_Anime_Movies_in_Hindi"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ sᴇʀɪᴇs ⛩", url=f"https://t.me/Anime_Series_in_Hindi_Dubbed"),
                InlineKeyboardButton(text="⛩ ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇs ⛩", url=f"https://t.me/Dub_Anime_Movies_in_Hindi"),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔂 ᴛʀʏ ᴀɢᴀɪɴ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔂 ᴛʀʏ ᴀɢᴀɪɴ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔂 ᴛʀʏ ᴀɢᴀɪɴ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
