import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# ================= Bot Information ====================
API_ID = int(environ.get("API_ID", "25399581"))
API_HASH = environ.get("API_HASH", "78e8a7d45e41484937c47acfdf1f6433")
BOT_TOKEN = environ.get("BOT_TOKEN", "7956117591:AAE5npKHm-NSJt-Noq82ihGJV_5Ot_9uYXk")
BOT_USERNAME = environ.get("BOT_USERNAME", "Sghvrgvbot")  # without @

# ================= Media & Admin ======================
PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split()
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6322672707').split()]

# ================= Port ===============================
PORT = environ.get("PORT", "8080")

# ================= Clone DB Config ====================
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "False"), False)
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://mohommediflaan:Zf0R9eAKTgs8jb6W@cluster0.hhpr2lx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# ================= Main DB Config =====================
DB_URI = environ.get("DB_URI", "mongodb+srv://mohommediflaan:Zf0R9eAKTgs8jb6W@cluster0.hhpr2lx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "mohommediflan")

# ================= Auto Delete Config =================
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "False"), False)
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800"))

# ================= Logging & Captions =================
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002768282561"))

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "📥 File ready to download!")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# ================= Feature Toggles ====================
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# ================= Shortlink / Verify =================
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "False"), False)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")

# ================= Website Streaming ==================
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "False"), False)
WEBSITE_URL = environ.get("WEBSITE_URL", "https://tamilben.blogspot.com/2025/06/bot.html")

# ================= File Streaming Config ==============
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "True"), True)
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "https://tamilben.blogspot.com/2025/06/bot.html")
