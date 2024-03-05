from telegram import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from src.constants import ButtonText, WEB_APP_URL

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(ButtonText.TASKS, web_app=WebAppInfo(f"{WEB_APP_URL}/")),
            KeyboardButton(
                ButtonText.PROFILE, web_app=WebAppInfo(f"{WEB_APP_URL}/profile")
            ),
        ]
    ]
)
