import aiohttp

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from telegram.constants import ChatAction

from src.constants import PB, PocketbaseCollections, BotReplies
from src.keyboards import MAIN_KEYBOARD
from src.helpers import fetch_user


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)

    async with aiohttp.ClientSession() as client:
        user_ = await PB.fetch_records(
            PocketbaseCollections.USERS,
            client,
            filter=f"tg_id=(tg_id='{update.effective_user.id}')",
        )

        if len(user_["items"]) != 0:
            user = user_["items"][0]

            if user["name"] != "":
                await update.message.reply_text(
                    BotReplies.ALSO_REGISTERED, reply_markup=MAIN_KEYBOARD
                )

                return ConversationHandler.END

            else:
                await update.message.reply_text(
                    BotReplies.USER_NAME,
                    reply_markup=MAIN_KEYBOARD,
                )

        else:
            await PB.add_record(
                PocketbaseCollections.USERS,
                client,
                tg_id=update.effective_user.id,
                username=update.effective_user.username,
                chat_id=update.effective_chat.id,
            )

            await update.message.reply_text(
                BotReplies.USER_NAME,
                reply_markup=MAIN_KEYBOARD,
            )

    return 1


async def get_user_name_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    async with aiohttp.ClientSession() as client:
        user = await fetch_user(update.effective_user.id, PB, client)

        await PB.update_record(
            PocketbaseCollections.USERS, user["id"], client, name=update.message.text
        )

    await update.message.reply_text(BotReplies.USER_NAME_UPLOADED)

    return ConversationHandler.END
