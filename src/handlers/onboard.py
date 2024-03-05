import aiohttp

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from telegram.constants import ChatAction

from src.constants import PB, PocketbaseCollections

from src.keyboards import MAIN_KEYBOARD

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)

    async with aiohttp.ClientSession() as client:
        await PB.add_record(
            PocketbaseCollections.USERS,
            client,
            tg_id=update.effective_user.id,
            username=update.effective_user.username,
            chat_id=update.effective_chat.id,
        )

    await update.message.reply_text(
        "START HANDLER STARTED",
        reply_markup=MAIN_KEYBOARD,
    )

    return 1