async def help(message):
    help_text = """
    ℹ️ *Ayuda y Soporte*
    • /start - Muestra el menú principal
    • /help - Muestra esta ayuda
    • /mycourses - Lista tus cursos
    • /viewcontent - Muestra contenido del curso
    • /submittask - Envía una tarea
    • /grades - Muestra tus calificaciones
    • /forum - Accede al foro
    • /progress - Muestra tu progreso
    • /register - Regístrate en un curso
    • /damecurso - Busca un curso específico
    """
    await message.answer(help_text, parse_mode="Markdown")