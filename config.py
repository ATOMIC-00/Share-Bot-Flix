#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6367580975:AAGGo8EUjgUWKnNrCAXou0_Ua86rvVednog")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20263428"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f9dc42564f6e6eb9920912b09f729e3f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001988634929"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1636310615"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Luciferbin:9339119160@cluster0.kmbiojj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "AiFileShare")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002154284624"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>👋 ʜɪ ᴅᴜᴅᴇ! 😎 {first}\n\nɪ’ᴍ ʏᴏᴜʀ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ! 📁✨\nʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ❗️</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ꜱᴏʀʀʏ ᴅᴜᴅᴇ ‼️ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ʏᴇᴛ.\n\nᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰɪʀꜱᴛ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ꜰɪʟᴇꜱ ‼️ 📂✨</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5437374877)
ADMINS.append(5052438254)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
