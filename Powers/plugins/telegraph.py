import os
from telegraph import upload_file
from pyrogram import  filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

START_TEXT = """Hello {},
I am an under 5MB media or file to telegra.ph link uploader Gojo.

Made by @FayasNoushad"""

HELP_TEXT = """**About Me**

- Just give me a media under 5MB
- Then I will download it
- I will then upload it to the telegra.ph link
"""

ABOUT_TEXT = """**About Me**

- **Gojo :** `Telegraph Uploader`
- **Developer :**
  • [GitHub](https://github.com/FayasNoushad)
  • [Telegram](https://telegram.me/FayasNoushad)
- **Source :** [Click here](https://github.com/FayasNoushad/Telegraph-Uploader-Gojo)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)"""



@Gojo.on_message(filters.command(["tgm"]) & filters.media)
async def getmedia(Gojo, update):
    
    medianame = DOWNLOAD_LOCATION + str(update.from_user.id)
    
    try:
        message = await update.reply_text(
            text="`Processing...`",
            quote=True,
            disable_web_page_preview=True
        )
        await Gojo.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        text=f"Error :- <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('More Help', callback_data='help')]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    
    text=f"**Link :-** `https://telegra.ph{response[0]}`\n\n**Join :-** @FayasNoushad"
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
            ],
            [
                InlineKeyboardButton(text="Join Updates Channel", url="https://telegram.me/FayasNoushad")
            ]
        ]
    )
    
    await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

