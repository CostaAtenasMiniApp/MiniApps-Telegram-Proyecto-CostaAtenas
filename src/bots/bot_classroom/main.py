# main.py
from bot import TelegramBot

if __name__ == "__main__":
    bot = TelegramBot("TU_TOKEN_DE_TELEGRAM")
    bot.start()