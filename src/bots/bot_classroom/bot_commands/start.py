# commands/start.py
from telegram import Update
from telegram.ext import CallbackContext
from .icommand import ICommand

class StartCommand(ICommand):
    async def execute(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text("🚀 ¡Bienvenido! Usa /help para ver comandos.")