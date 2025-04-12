from .icommand import ICommand
from telegram import Update
from telegram.ext import CallbackContext

class ShowProgressInCourseCommand(ICommand):
    async def execute(self, update: Update, context: CallbackContext) -> None:
        # Lógica para mostrar el progreso en el curso
        await update.message.reply_text("📈 Este es tu progreso en el curso:")