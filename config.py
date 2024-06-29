# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7314346623:AAGthfZirCo-EUVBkTyp1UOh2BUNVajSosI")
APP_ID = int(os.environ.get("APP_ID", "23873858"))
API_HASH = os.environ.get("API_HASH", "bfc7ff263795b22bb7065abe95bed3a2")


OWNER = os.environ.get("OWNER", "@Patel_080") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "5284816025")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://sunitverma080:4LYZiim5L31SCNBz@realfree.3s31w2j.mongodb.net/?retryWrites=true&w=majority&appName=Realfree")
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002147039566"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002219866724"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "100"))




START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "5857939104 5284816025 5857939104 6367302898").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(5284816025)
ADMINS.append(5284816025)

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
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
