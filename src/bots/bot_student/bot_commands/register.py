# commands/register.py
from .icommand import ICommand
from telegram import Update
from telegram.ext import CallbackContext
from states.registration_state_machine import RegistrationStateMachine  # Implementación de State Pattern

class RegisterCommand(ICommand):
    async def execute(self, update: Update, context: CallbackContext) -> None:
        user_id = update.effective_user.id
        context.user_data[user_id] = RegistrationStateMachine()
        await update.message.reply_text("📝 Ingresa tu nombre:")