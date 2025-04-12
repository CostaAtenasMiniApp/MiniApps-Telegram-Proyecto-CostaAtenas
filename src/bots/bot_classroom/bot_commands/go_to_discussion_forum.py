from .icommand import ICommand
from telegram import Update
from telegram.ext import CallbackContext

class GoToDiscussionforumCommand(ICommand):
    async def execute(self, update: Update, context: CallbackContext) -> None:
        # Lógica para redirigir al foro de discusión
        await update.message.reply_text("💬 Redirigiendo al foro de discusión...")