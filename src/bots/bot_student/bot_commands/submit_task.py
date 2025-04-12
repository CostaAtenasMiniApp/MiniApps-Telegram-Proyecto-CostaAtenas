from .icommand import ICommand
from telegram import Update
from telegram.ext import CallbackContext

class SubmitTaskCommand(ICommand):
    async def execute(self, update: Update, context: CallbackContext) -> None:
        # Lógica para enviar una tarea completada
        await update.message.reply_text("✅ Tarea enviada correctamente.")