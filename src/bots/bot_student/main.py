# main.py
from bot import TelegramBot
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("StudientCifPlayasBot")
    bot = TelegramBot(token)
    bot.start()