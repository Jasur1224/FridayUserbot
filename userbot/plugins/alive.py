
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://t.me/HTTP_URL/6"
ALIVE_caption = "`🤖SHAXSIY ROBOT🤖:` **ON-LINE**\n\n"
ALIVE_caption += "**🛠️ROBOT HOLATI🛠️**\n\n"
ALIVE_caption += "`🎲TELETHON VERSIYASI:` **6.0.9**\n`Python:` **3.7.4**\n\n"
ALIVE_caption += "`💾MALUMOTLAR BAZASI:` **FUNKSIYONAL**\n\n"
ALIVE_caption += "**Current Branch** : `master`\n\n"
ALIVE_caption += "**Friday OS** : `3.14`\n\n"
ALIVE_caption += "**Current Sat** : `StarkGangSat-2.25`\n\n"
ALIVE_caption += f"**My Boss** : {DEFAULTUSER} \n\n"
ALIVE_caption += "**💽HEROKU MALUMOTLAR BAZASI** : `AWS - SERVERI ISHLAYAPTI`\n\n"
ALIVE_caption += "**🗂️LITSENZIYA** : [😝😝😝😝😝](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n\n"
ALIVE_caption += "MUALLIFLIK HUQUQI: [Jasur Abdurahmonov](GitHub.com/Jasur1224)\n\n"
ALIVE_caption += "[ROBOT EGASI](https://t.me/uzbekman_ok)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)
