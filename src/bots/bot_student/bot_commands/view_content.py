from .icommand import ICommand
from telegram import Update
from telegram.ext import CallbackContext

class ViewContentCommand(ICommand):
    async def execute(self, update: Update, context: CallbackContext) -> None:
        # Lógica para listar el contenido del curso
        await update.message.reply_text("📖 Aquí está el contenido del curso:")