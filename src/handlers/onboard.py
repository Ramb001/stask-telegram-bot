import aiohttp

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from telegram.constants import ChatAction

from src.constants import PB, PocketbaseCollections, BotReplies
from src.keyboards import ON_BOARD_KEYBOARD, create_main_keyboard
from src.helpers import fetch_user


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)

    async with aiohttp.ClientSession() as client:
        user_ = await PB.fetch_records(
            PocketbaseCollections.USERS,
            client,
            filter=f"tg_id=(tg_id='{update.effective_user.id}')",
        )

        if len(user_["items"]) == 0:
            await PB.add_record(
                PocketbaseCollections.USERS,
                client,
                tg_id=update.effective_user.id,
                username=update.effective_user.username,
                chat_id=update.effective_chat.id,
            )

    await update.message.reply_text(
        BotReplies.HAVE_REF,
        reply_markup=ON_BOARD_KEYBOARD,
    )

    return 1


async def yes_ref_link_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(
        update.effective_chat.id, BotReplies.SEND_REF_LINK, reply_markup=""
    )

    return 2


async def add_to_org_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text is None:
        return 2

    async with aiohttp.ClientSession() as client:
        organization_ = await PB.fetch_records(
            PocketbaseCollections.ORGANIZATIONS,
            client,
            filter=f"(ref_link='{update.message.text}')",
        )

        if len(organization_["items"]) == 0:
            await context.bot.send_message(
                update.effective_chat.id,
                BotReplies.NO_ORGANIZATIONS_BY_LINK,
                reply_markup=create_main_keyboard(update),
            )
        else:
            organization = organization_["items"][0]
            user = await fetch_user(update.effective_user.id, PB, client)

            organization["workers"].append(user["id"])

            await PB.update_record(
                PocketbaseCollections.ORGANIZATIONS,
                organization["id"],
                client,
                workers=organization["workers"],
            )

            await context.bot.send_message(
                update.effective_chat.id,
                BotReplies.ADDED_TO_ORGANIZATION.format(
                    organization_name=organization["name"]
                ),
                reply_markup=create_main_keyboard(update),
            )

    return ConversationHandler.END


async def no_ref_link_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id,
        BotReplies.WELCOME,
        reply_markup=create_main_keyboard(update),
    )

    return ConversationHandler.END
