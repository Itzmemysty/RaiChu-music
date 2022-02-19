## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "9189658"))
API_HASH = getenv("API_HASH", "292b82ffbe110c821bc6d6db4f37d34d")
OWNER_NAME = getenv("OWNER_NAME", "亗 ❥︎×͜×『Mʏsᴛᴇʀɪᴏᴜs』❥︎࿐亗")
ALIVE_NAME = getenv("ALIVE_NAME", "💘💞✰★𝙆𝙖𝙣𝙣𝙞 𝙍𝙖𝙖𝙨𝙞 𝙆𝙖𝙖𝙧𝙖𝙣 𝘿𝙖★✰💞💘")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Itz_meAlien")
BOT_USERNAME = getenv("BOT_USERNAME", "Itxmealienbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "🛸👽🇦 ꪶ𝓲ꫀꪀ👽🛸")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "itzmealiensupportgroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "itzmealienUpdates")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4474a086aa25afd91bf2d.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/714f0185c6de1aa3054e0.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/29776449e7e5b64f9a3ff.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/af3099e33051a1bd4023a.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/a905686e19c935952c9cf.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/9cc2d4e2c1971d68ab138.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/38421751a52a2f32d237f.jpg")
IMG_7 = getenv("IMG_7", "https://telegra.ph/file/ea52c7e59a622f051d5a5.jpg")
IMG_8 = getenv("IMG_8", "https://telegra.ph/file/8062c42640e9b48e1cf28.jpg")
IMG_9 = getenv("IMG_9", "https://telegra.ph/file/5658c84881d7e5d6aa446.jpg")
IMG_10= getenv("IMG_10","https://telegra.ph/file/df46d0b76a3e5faa52859.jpg")
