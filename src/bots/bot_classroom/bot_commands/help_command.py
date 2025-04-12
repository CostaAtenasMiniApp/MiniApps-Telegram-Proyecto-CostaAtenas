from typing import Dict, Type
from telegram import Update
from telegram.ext import CallbackContext
from .icommand import ICommand # Importamos la interfaz base

class HelpCommand(ICommand):
    def __init__(self, available_commands: Dict[str, str]):
        """
        :param available_commands: Diccionario con {nombre_comando: descripción}
        """
        self._available_commands = available_commands

    async def execute(self, update: Update, context: CallbackContext) -> None:
        help_text = "🛠️ <b>Comandos disponibles:</b>\n\n"

        # Genera la lista de comandos y sus descripciones
        for cmd, description in self._available_commands.items():
            help_text += f"• /{cmd}: <i>{description}</i>\n"

        help_text += "\nℹ️ Usa /help [comando] para más detalles."
        await update.message.reply_text(help_text, parse_mode="HTML")