# bot.py
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram import Update
from handlers import CommandRouter

class TelegramBot:
    def __init__(self, token: str):
        self._application = Application.builder().token(token).build()
        self._router = CommandRouter()  # Inyecta el router

    def start(self):
        # Mapeo dinámico de comandos
        self._application.add_handler(CommandHandler("start", self._handle_command))
        self._application.add_handler(CommandHandler("help", self._handle_command))
        self._application.add_handler(CommandHandler("register", self._handle_command))
        self._application.add_handler(CommandHandler("mycourses", self._handle_command))
        self._application.add_handler(CommandHandler("viewcontent", self._handle_command))
        self._application.add_handler(CommandHandler("submittask", self._handle_command))
        self._application.add_handler(CommandHandler("grades", self._handle_command))
        self._application.add_handler(CommandHandler("forum", self._handle_command))
        self._application.add_handler(CommandHandler("progress", self._handle_command))

        # Manejador para comandos no definidos
        self._application.add_handler(MessageHandler(filters.COMMAND, self._handle_unknown_command))

        # Manejo de mensajes no comandos
        self._application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))

        self._application.run_polling()

    async def _handle_unknown_command(self, update: Update, context: CallbackContext):
        await update.message.reply_text("⚠️ Lo siento, no reconozco ese comando. Usa /help para ver los comandos disponibles.")

    async def _handle_command(self, update: Update, context: CallbackContext):
        command_name = update.message.text.split()[0][1:]  # Extrae "start" de "/start"
        await self._router.handle(command_name, update, context)

    def _handle_message(self, update: Update, context: CallbackContext) -> None:
        user_id = update.effective_user.id
        if user_id in context.user_data:  # Si hay un estado activo (ej: registro)
            state_machine = context.user_data[user_id]
            response = state_machine.handle(update.message.text)
            update.message.reply_text(response)
