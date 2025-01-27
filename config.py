import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
NOTIFY_CHANNEL_ID = int(os.getenv("NOTIFY_CHANNEL_ID"))
