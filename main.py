import logging
import os

from telegram.ext import (
    ApplicationBuilder,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.constants import TOKEN
from src.handlers.onboard import start_handler, get_user_name_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    onboard_conv = ConversationHandler(
        entry_points=[CommandHandler("start", start_handler)],
        states={
            1: [MessageHandler(filters.TEXT, get_user_name_handler)],
        },
        fallbacks=[],
    )

    app.add_handler(onboard_conv)

    while True:
        app.run_polling()


if __name__ == "__main__":
    main()
