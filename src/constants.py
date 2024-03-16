import os

from src.pocketbase import Pocketbase


POCKETBASE_URL = "http://127.0.0.1:8090"
PB = Pocketbase(POCKETBASE_URL)
TOKEN = os.getenv("STASK_BOT_TOKEN")
WEB_APP_URL = "https://33d9-178-66-131-169.ngrok-free.app"


class PocketbaseCollections:
    USERS = "users"
    ORGANIZATIONS = "organizations"


class ButtonText:
    TASKS = "View tasks 💬"
    PROFILE = "Profile 👨‍💻"
    YES = "Yes ✅"
    NO = "No ❌"


class BotReplies:
    ALSO_REGISTERED = "You also registered"
    HAVE_REF = "Do you have invitation link to organization?"
    SEND_REF_LINK = "Send your invitation link to join to organization"
    NO_ORGANIZATIONS_BY_LINK = "Sorry, but no one organization was found!"
    ADDED_TO_ORGANIZATION = (
        "You was added to {organization_name} as a worker.\n Welcome to Stask!"
    )
    WELCOME = "Welcome to Stask!"


class CallbackQuery:
    YES_REF = "yes_ref"
    NO_REF = "no_ref"
