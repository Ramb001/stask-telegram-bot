import os

from src.pocketbase import Pocketbase


POCKETBASE_URL = "http://45.143.94.202:8090"
PB = Pocketbase(POCKETBASE_URL)
TOKEN = os.getenv("STASK_BOT_TOKEN")
WEB_APP_URL = "https://362a-178-66-159-229.ngrok-free.app"


class PocketbaseCollections:
    USERS = "users"
    ORGANIZATIONS = "organizations"
    TASKS = "tasks"


class WebAppActions:
    CREATE_TASK = "create_task"


class TaskStatuses:
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    DONE = "done"


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
    CREATED_TASK = "<b>New task</b> in {organization_name}!\n<b>Title:</b> {title}\n<b>Description:</b> {description}\n<b>Workers:</b> {workers}"


class CallbackQuery:
    YES_REF = "yes_ref"
    NO_REF = "no_ref"
