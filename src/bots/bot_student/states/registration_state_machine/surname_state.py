from .state import State
from .email_state import EmailState

class SurnameState(State):
    def handle(self, update, context):
        surname = update.message.text
        if surname.isalpha():
            self.machine.transition_to(EmailState(self.machine))
            update.message.reply_text("Por favor, ingresa tu correo electrónico:")
        else:
            update.message.reply_text("⚠️ Los apellidos no pueden contener números. Inténtalo de nuevo:")
