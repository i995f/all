import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "23547316"))
API_HASH = getenv("API_HASH", "a610ab618939db27b40bd285a09ce46c")
BOT_TOKEN = getenv("BOT_TOKEN", "5575266884:AAFitGGF7lVIV7iacGE8aaIGpXDxa_3FaF8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgFnTbQANYj5FfjhR3qPz2Fn45oMvip-P8W_JAHgZxjJ1crKJj5oDndP5_grYuZ9Yxrq9h0wkKvHN6bRjtJHgxeng1dZsT2kiLAiirTyPXgakXB7k9x0bSTzPOylXVLSLln-IqGaXgXD40xkqgdHdnHysOtWRmaFAq_qT2GyVy8otFrNyn1kdkBAm025NxzKf2aV3_R2_FjFbd50oR5-OjKu8ccbqtPuXSB0d71XIFq-PUyuw2h3J4HM01581UueXoy1cRYQnKkB0nLO7Rvy8s3HEg4Zff-lrLVLVer-uQtepXCOVOxy_QI5Tgmy_cUQcHQVW0oy9z6aKnfImU4RmCWsVuP-UAAAAAFylWwYAA")
BOT_USERNAME = getenv("BOT_USERNAME", "H4CHBOT")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5784465297").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5784465297").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001832430541")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "TTidT")
GROUP = getenv("GROUP", "TTidT")
BOT_NAME = getenv("BOT_NAME", "Shai")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


