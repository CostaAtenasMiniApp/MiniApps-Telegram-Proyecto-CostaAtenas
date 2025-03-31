# commands/register.py
from src.bots.bot_classroom.commands.Command import Command
from telegram import Update
from telegram.ext import CallbackContext
from states.registration_state_machine import RegistrationStateMachine  # Implementación de State Pattern

class RegisterCommand(Command):
    def execute(self, update: Update, context: CallbackContext) -> None:
        user_id = update.effective_user.id
        context.user_data[user_id] = RegistrationStateMachine()
        update.message.reply_text("📝 Ingresa tu nombre:")