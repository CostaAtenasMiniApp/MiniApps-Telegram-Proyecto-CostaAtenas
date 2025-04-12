from .icommand import ICommand
from telegram import Update
from telegram.ext import CallbackContext

class gradesCommand(ICommand):
    async def execute(self, update: Update, context: CallbackContext) -> None:
        # Lógica para mostrar las calificaciones
        await update.message.reply_text("📊 Estas son tus calificaciones:")