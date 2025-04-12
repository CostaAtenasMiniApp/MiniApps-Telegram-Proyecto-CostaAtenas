async def start(message):
    welcome_text = """
    🎓 *Bienvenido al Bot de Cursos* 🎓
    Comandos disponibles:
    /start - Menú principal
    /help - Ayuda y soporte
    /mycourses - Tus cursos inscritos
    /viewcontent - Contenido disponible
    /submittask - Enviar tarea
    /grades - Ver calificaciones
    /forum - Acceder al foro
    /progress - Tu progreso
    /register - Registrarte en un curso
    /damecurso - Buscar curso específico
    """
    await message.answer(welcome_text, parse_mode="Markdown")