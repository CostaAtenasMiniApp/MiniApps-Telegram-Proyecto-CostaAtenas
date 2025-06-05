from abc import ABC, abstractmethod
import telebot
from telebot import types

class TelegramBotTemplate(ABC):
    def __init__(self, token: str):
        self.bot = telebot.TeleBot(token)
    
    @abstractmethod
    def start_command(self, message: types.Message) -> None:
        """Maneja el comando /start."""
        pass

    @abstractmethod
    def help_command(self, message: types.Message) -> None:
        """Maneja el comando /help."""
        pass

    @abstractmethod
    def handle_text(self, message: types.Message) -> None:
        """Maneja mensajes de texto genéricos."""
        pass

    @abstractmethod
    def handle_photo(self, message: types.Message) -> None:
        """Maneja envío de fotos."""
        pass

    @abstractmethod
    def setup_handlers(self) -> None:
        """Configura los manejadores (handlers) del bot."""
        pass

    @abstractmethod
    def run(self) -> None:
        """Inicia el bot (polling o webhook)."""
        pass
