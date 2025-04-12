from .state import State
from src.infrastructure.repositories.student_repository import StudentRepository
class ConfirmationCodeState(State):
    async def handle(self, update, context):
        confirmation_code = update.message.text
        if confirmation_code == "1234":  # Ejemplo de código de confirmación
            # Obtener datos del estudiante desde user_data
            user_data = context.user_data.get(update.effective_user.id, {})
            name = user_data.get("name")
            surname = user_data.get("surname")
            email = user_data.get("email")

            # Guardar estudiante en la base de datos
            student_repository = StudentRepository()
            await student_repository.create_student(name=f"{name} {surname}", email=email)

            update.message.reply_text("✅ Registro completado. ¡Bienvenido!")
        else:
            update.message.reply_text("⚠️ Código de confirmación incorrecto. Inténtalo de nuevo.")
