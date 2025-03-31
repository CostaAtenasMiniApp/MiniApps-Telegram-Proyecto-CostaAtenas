from .state import State

class ConfirmationCodeState(State):
    def handle(self, update, context):
        code = update.message.text
        if code.isdigit():
            update.message.reply_text("✅ Registro completado con éxito.")
            self.machine.state = None  # Finaliza el proceso
        else:
            update.message.reply_text("⚠️ El código de confirmación debe ser numérico. Inténtalo de nuevo:")
