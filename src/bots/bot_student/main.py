# main.py
from src.bots.bot_student.bot import TelegramBot
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    token = os.getenv("StudientCifPlayasBot")
    bot = TelegramBot(token)
    bot.start()