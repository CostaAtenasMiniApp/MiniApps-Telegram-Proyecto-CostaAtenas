from .icommand import ICommand
from telegram import Update
from telegram.ext import ContextTypes

class ListPersonalCoursesCommand(ICommand):
    async def execute(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Lógica para listar los cursos personales
        await update.message.reply_text("📚 Aquí están tus cursos personales:")