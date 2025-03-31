# handlers.py
from commands import StartCommand, HelpCommand, RegisterCommand

class CommandRouter:
    def __init__(self):
        self._commands = {
            "start": StartCommand(),
            "help": HelpCommand(),
            "register": RegisterCommand(),
            # ... añade más comandos aquí
        }

    def handle(self, command_name: str, update: Update, context: CallbackContext) -> None:
        command = self._commands.get(command_name)
        if command:
            command.execute(update, context)
        else:
            update.message.reply_text("⚠️ Comando no reconocido. Usa /help")