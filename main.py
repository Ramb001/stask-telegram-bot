import logging
import os

from telegram.ext import (
    ApplicationBuilder,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from src.constants import TOKEN, CallbackQuery
from src.handlers.onboard import (
    start_handler,
    yes_ref_link_handler,
    no_ref_link_handler,
    add_to_org_handler,
)

from src.handlers.web_app import web_app_data_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    onboard_conv = ConversationHandler(
        entry_points=[CommandHandler("start", start_handler)],
        states={
            1: [
                CallbackQueryHandler(yes_ref_link_handler, CallbackQuery.YES_REF),
                CallbackQueryHandler(no_ref_link_handler, CallbackQuery.NO_REF),
            ],
            2: [MessageHandler(filters.TEXT, add_to_org_handler)],
        },
        fallbacks=[],
    )

    app.add_handler(onboard_conv)
    app.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data_handler)
    )

    while True:
        app.run_polling()


if __name__ == "__main__":
    main()
