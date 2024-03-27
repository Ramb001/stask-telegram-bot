import html
import json

import aiohttp
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from src.constants import (
    PB,
    BotReplies,
    WebAppActions,
    TaskStatuses,
    PocketbaseCollections,
)
from src.helpers import fetch_organization, fetch_user


async def web_app_data_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    action = json.loads(update.effective_message.web_app_data.data)
    if action["action"] == WebAppActions.CREATE_TASK:
        await __handle_create_task(update, context, action)
    elif action["action"] == WebAppActions.CREATE_ORGANIZATION:
        await __handle_create_organization(update, context, action)


async def __handle_create_task(
    update: Update, context: ContextTypes.DEFAULT_TYPE, action: dict
):
    data = action["data"]
    async with aiohttp.ClientSession() as client:
        organization = await fetch_organization(data["organization"], PB, client)
        creator = await fetch_user(data["creator"], PB, client)

        await PB.add_record(
            PocketbaseCollections.TASKS,
            client,
            title=data["title"],
            description=data["description"],
            organization=organization["id"],
            creator=creator["id"],
            workers=[worker["id"] for worker in data["workers"]],
            deadline=data["deadline"],
            status=TaskStatuses.NOT_STARTED,
        )

        await context.bot.send_message(
            update.effective_chat.id,
            text=BotReplies.CREATED_TASK.format(
                organization_name=data["organization"],
                title=data["title"],
                description=data["description"],
                workers=", ".join(
                    (
                        worker["name"]
                        if len(worker["name"]) != 0
                        else f"@{worker['username']}"
                    )
                    for worker in data["workers"]
                ),
            ),
            parse_mode=ParseMode.HTML,
        )

    for worker in data["workers"]:
        if worker["id"] != organization["owner"]:
            await context.bot.send_message(
                worker["chat_id"],
                text=BotReplies.CREATED_TASK.format(
                    organization_name=data["organization"],
                    title=data["title"],
                    description=data["description"],
                    workers=", ".join(
                        (
                            worker["name"]
                            if len(worker["name"]) != 0
                            else f"@{worker['username']}"
                        )
                        for worker in data["workers"]
                    ),
                ),
                parse_mode=ParseMode.HTML,
            )


async def __handle_create_organization(
    update: Update, context: ContextTypes.DEFAULT_TYPE, action: dict
):
    data = action["data"]
    print(data)
    async with aiohttp.ClientSession() as client:
        owner = await fetch_user(data["owner"], PB, client)

        await PB.add_record(
            PocketbaseCollections.ORGANIZATIONS,
            client,
            name=data["name"],
            owner=owner["id"],
            ref_link=data["ref_link"],
        )

        await context.bot.send_message(
            update.effective_chat.id,
            text=BotReplies.CREATED_ORGANIZATION.format(
                organization_name=data["name"], ref_link=data["ref_link"]
            ),
            parse_mode=ParseMode.HTML,
        )
