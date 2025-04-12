from .state import State
from .email_state import EmailState

class SurnameState(State):
    def handle(self, update, context):
        surname = update.message.text
        if surname.isalpha():
            # Guardar los apellidos en user_data
            user_data = context.user_data.get(update.effective_user.id, {})
            user_data["surname"] = surname
            context.user_data[update.effective_user.id] = user_data

            self.machine.transition_to(EmailState(self.machine))
            update.message.reply_text("Por favor, ingresa tu correo electrónico:")
        else:
            update.message.reply_text("⚠️ Los apellidos no pueden contener números. Inténtalo de nuevo:")
