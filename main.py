import logging 
import os

from telegram.ext import ApplicationBuilder, ConversationHandler, CommandHandler

from src.constants import TOKEN
from src.handlers.onboard import start_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    app = ApplicationBuilder().token(TOKEN).build()


    onboard_conv =CommandHandler("start", start_handler)
    
    app.add_handler(onboard_conv)

    while True:
        app.run_polling()


if __name__ == "__main__":
    main()