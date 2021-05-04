from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**┗┓| RASCALS BOT MUSIK | ┏┛**

**Hallo kamu** 🙋‍♂
Nama saya adalah __[Rascals Music Assisten Bot](https://t.me/Rascals_MusicBot)__
Saya bisa memutar musik di **Voice Call Grup** kamu
━━━━━━━━━━━━━━━━━━━━
Dikelola oleh **[Yunus Zend](https://t.me/ZendYNS)**

❖ **Tambahkan __[Rascals Music Assistant](https://t.me/Rascals_MusicAssistant)__ dan [Rascals Music Bot](https://t.me/Rascals_MusicBot)__ ke grup Anda, dan rasakan sensasi mendengar musik di VC Group anda!!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 More Info 🎧", url="https://github.com/ImJanindu/GroupMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "💭 Group Support", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Creator 👨‍💻", url="https://t.me/ZendYNS"
                    ),
                    InlineKeyboardButton(
                        "Channel Support 🔉", url="https://t.me/UpdateInfoBOT"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Infinity_BOTs")
                ]
            ]
        )
   )


