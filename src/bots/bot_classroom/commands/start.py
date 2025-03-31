# commands/start.py
from telegram import Update
from telegram.ext import CallbackContext
from src.bots.bot_classroom.commands.Command import Command

class StartCommand(Command):
    def execute(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text("🚀 ¡Bienvenido! Usa /help para ver comandos.")