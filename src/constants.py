import os

from src.pocketbase import Pocketbase


POCKETBASE_URL = "http://127.0.0.1:8090"
PB = Pocketbase(POCKETBASE_URL)
TOKEN = os.getenv("STASK_BOT_TOKEN")
WEB_APP_URL = "https://33d9-178-66-131-169.ngrok-free.app"


class PocketbaseCollections:
    USERS = "users"


class ButtonText:
    TASKS = "View tasks 💬"
    PROFILE = "Profile 👨‍💻"


class BotReplies:
    USER_NAME = "Type your name (ex. Name Surname)"
    USER_NAME_UPLOADED = "Thanks for registration"
    ALSO_REGISTERED = "You also registered"
