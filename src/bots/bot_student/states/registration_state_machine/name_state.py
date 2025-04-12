from .state import State
from .surname_state import SurnameState

class NameState(State):
    def handle(self, update, context):
        name = update.message.text
        if name.isalpha():
            # Guardar el nombre en user_data
            context.user_data[update.effective_user.id] = {"name": name}
            self.machine.transition_to(SurnameState(self.machine))
            update.message.reply_text("Por favor, ingresa tus apellidos:")
        else:
            update.message.reply_text("⚠️ El nombre no puede contener números. Inténtalo de nuevo:")
