from .state import State
from .confirmation_code_state import ConfirmationCodeState

class EmailState(State):
    def handle(self, update, context):
        email = update.message.text
        if "@" in email and "." in email:
            self.machine.transition_to(ConfirmationCodeState(self.machine))
            update.message.reply_text("Por favor, ingresa el código de confirmación:")
        else:
            update.message.reply_text("⚠️ El correo electrónico no es válido. Inténtalo de nuevo:")
