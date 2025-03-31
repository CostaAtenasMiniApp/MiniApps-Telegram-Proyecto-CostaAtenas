from telegram import Update
from telegram.ext import CallbackContext


from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, update: Update, context: CallbackContext) -> None:
        pass