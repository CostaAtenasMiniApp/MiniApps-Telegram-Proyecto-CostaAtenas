# bot.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from handlers import CommandRouter

class TelegramBot:
    def __init__(self, token: str):
        self._updater = Updater(token)
        self._router = CommandRouter()  # Inyecta el router

    def start(self):
        dispatcher = self._updater.dispatcher

        # Mapeo dinámico de comandos
        dispatcher.add_handler(CommandHandler("start", self._handle_command))
        dispatcher.add_handler(CommandHandler("help", self._handle_command))
        dispatcher.add_handler(CommandHandler("register", self._handle_command))

        # Manejo de mensajes no comandos
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self._handle_message))

        self._updater.start_polling()

    def _handle_command(self, update: Update, context: CallbackContext) -> None:
        command_name = update.message.text.split()[0][1:]  # Extrae "start" de "/start"
        self._router.handle(command_name, update, context)

    def _handle_message(self, update: Update, context: CallbackContext) -> None:
        user_id = update.effective_user.id
        if user_id in context.user_data:  # Si hay un estado activo (ej: registro)
            state_machine = context.user_data[user_id]
            response = state_machine.handle(update.message.text)
            update.message.reply_text(response)