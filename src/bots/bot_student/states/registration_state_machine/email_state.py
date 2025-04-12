from .state import State
from .confirmation_code_state import ConfirmationCodeState

class EmailState(State):
    def handle(self, update, context):
        email = update.message.text
        if "@" in email and "." in email:
            # Guardar el correo en user_data
            user_data = context.user_data.get(update.effective_user.id, {})
            user_data["email"] = email
            context.user_data[update.effective_user.id] = user_data

            self.machine.transition_to(ConfirmationCodeState(self.machine))
            update.message.reply_text("Por favor, ingresa el código de confirmación:")
        else:
            update.message.reply_text("⚠️ El correo electrónico no es válido. Inténtalo de nuevo:")
