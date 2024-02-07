
"""
telegram]
api_id = "2568615"
api_hash = "1e62cca9207a4469ca847526acebb660"

[tekegram.bot]
bot_token = "6956874781:AAGzsdSn3rSahmDx5hxlu9N6SvEFycubg_8"
name = "Elaina"
username = "@Elaina"
user_id = "2069340770"

[database]
database_url = "mongodb+srv://elianaapi:pranav8935@cluster0.gf5ky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

[settings]
owner = "1194169408"
sudo_users = ['1194169408']

[settings.commands]
prefix = ['!', '/']

[settings.log]
chat_id = "-1001251337410"

[settings.backup]
chat_id = "-1001251337410"
"""
from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN =  "6956874781:AAGzsdSn3rSahmDx5hxlu9N6SvEFycubg_8"
    API_ID = int("2568615")
    API_HASH = "1e62cca9207a4469ca847526acebb660"
    OWNER_ID = int("1194169408")
    MESSAGE_DUMP = int("1001251337410")
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="",
        ).split(None)
    ]
#    GENIUS_API_TOKEN = "aehsxwAsU4s441PAg2U7wKuhSdy"
#    AuDD_API = "c650cc651432caab4dc63d6b2c912406"
#    RMBG_API = config("RMBG_API",default=None)
    DB_URI = "mongodb+srv://happykira4500:papajee1-1@cluster0.vdvdkly.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME =  "elianaapi"
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""
    owner_username = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "YOUR BOT_TOKEN"
    API_ID = 12345  # Your APP_ID from Telegram
    API_HASH = "YOUR API HASH"  # Your APP_HASH from Telegram
    OWNER_ID = 1344569458  # Your telegram user id defult to mine
    MESSAGE_DUMP = -100845454887  # Your Private Group ID for logs
    DEV_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://happykira4500:papajee1-1@cluster0.vdvdkly.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "happykira4500"  # Your DB name
    NO_LOAD = []
 #   GENIUS_API_TOKEN = ""
#    RMBG_API = ""
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "SUPPORT_GROUP"
    SUPPORT_CHANNEL = "SUPPORT_CHANNEL"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
