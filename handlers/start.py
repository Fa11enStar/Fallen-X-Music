import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**๐ สษชแดแด แดแดแดษด {message.from_user.mention()} !

        แดสษชs ษชs [{bn}](t.me/{bu}), Aษด แดแดแด แดษดแดแด แดแดsษชแด สแดแด๐


โโโโโโโโโโโโโโโโ
โฃโธโกโโโฃโโ โโจ: [@ARG_GAMING_9300]
โฃ6๐๐ต-๐๐ฒ๐ป ๐ถ๐ป๐ฏ๐๐ถ๐น๐ ๐๐๐๐๐ฒ๐บ๐
โฃเผ๏ธ๐๐ถ๐๐ฒ๐ฐ๐ต ๐๐ป๐ด๐ถ๐ป๐ฒเผ๏ธ
โฃ๐๐๐๐  ๐๐ซ๐๐ & ๐ฎ๐ฅ๐ญ๐ซ๐ ๐ช๐ฎ๐๐ฅ๐ข๐ญ๐ฒ๐
โฃ๐ฏ๐ ๐ผ๐ฟ๐ฒ ๐ณ๐ฒ๐ฎ๐๐๐๐ฟ๐ฒ๐ ๐๐ผ๐ผ๐ป๐ฏ
โฃ ๐๐ง๐๐๐บ ๐ณ๐ผ๐ฟ ๐๐๐ถ๐ป๐ด ๐๐ !!!
โโโโโโโโโโโโโโโโ

๐ ๊ฐแดส แดษดส วซแดแดสษชแดs แดแด @ARG_GAMING_9300 ๐ฆ**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅบ แดแดแด แดสแด ษดแด สแดสส ๐ฅบ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "๐ แดแดกษดแดส ๐", url="https://t.me/ARG_GAMING_9300"
                    ),
                    InlineKeyboardButton(
                        "๐ sแดแดแดแดสแด ๐", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "๐ฆ แดsส แดสแดษด ๐ฆ", url= "https://t.me/TSH_CLAN_ORG"
                    ),
                    InlineKeyboardButton(
                        "๐พ sแดแดสแดแด แดแดแดแด ๐พ", url="https://github.com/ARGGAMING777/ARG-X-Alexia"
                    )]
            ]
       ),
    )

