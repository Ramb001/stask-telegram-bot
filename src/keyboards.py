from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from src.constants import ButtonText, WEB_APP_URL, CallbackQuery

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(ButtonText.TASKS, web_app=WebAppInfo(f"{WEB_APP_URL}/"))],
        [
            KeyboardButton(
                ButtonText.PROFILE, web_app=WebAppInfo(f"{WEB_APP_URL}/profile")
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
