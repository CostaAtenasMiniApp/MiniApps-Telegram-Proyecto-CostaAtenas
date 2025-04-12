# handlers.py
from bot_commands import (
    StartCommand, HelpCommand, RegisterCommand,
    ListPersonalCoursesCommand, ViewContentCommand,
    SubmitTaskCommand, gradesCommand,
    GoToDiscussionforumCommand, ShowProgressInCourseCommand
)
from telegram import Update
from telegram.ext import CallbackContext

class CommandRouter:
    def __init__(self):
        available_commands = {
            'start': 'Mostrar menú principal y opciones disponibles',
            'mycourses': 'Listar cursos en los que estás inscrito',
            'viewcontent': 'Mostrar contenido disponible del curso',
            'submittask': 'Enviar una tarea completada',
            'grades': 'Mostrar calificaciones obtenidas',
            'forum': 'Acceder al foro de discusión del curso',
            'progress': 'Mostrar progreso en el curso',
            'help': 'Mostrar ayuda y soporte disponible'
        }
        self._commands = {
            "start": StartCommand(),
            "help": HelpCommand(available_commands),
            "register": RegisterCommand(),
            "mycourses": ListPersonalCoursesCommand(),
            "viewcontent": ViewContentCommand(),
            "submittask": SubmitTaskCommand(),
            "grades": gradesCommand(),
            "forum": GoToDiscussionforumCommand(),
            "progress": ShowProgressInCourseCommand(),
            # ... add more commands here
        }

    async def handle(self, command_name: str, update: Update, context: CallbackContext):
        command = self._commands.get(command_name)
        if command:
            await command.execute(update, context)
        else:
            update.message.reply_text("⚠️ Comando no reconocido. Usa /help")