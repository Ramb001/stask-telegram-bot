from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Update,
)
from urllib.parse import urlencode

from src.constants import ButtonText, WEB_APP_URL, CallbackQuery


def create_main_keyboard(update: Update):
    params = urlencode(
        {
            "user_id": update.effective_user.id,
            "language_code": update.effective_user.language_code,
        }
    )
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(
                    ButtonText.TASKS, web_app=WebAppInfo(f"{WEB_APP_URL}/?{params}")
                )
            ],
            [
                KeyboardButton(
                    ButtonText.PROFILE,
                    web_app=WebAppInfo(f"{WEB_APP_URL}/profile?{params}"),
                )
            ],
        ],
        resize_keyboard=True,
    )


ON_BOARD_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(ButtonText.YES, callback_data=CallbackQuery.YES_REF),
            InlineKeyboardButton(ButtonText.NO, callback_data=CallbackQuery.NO_REF),
        ],
    ]
)
