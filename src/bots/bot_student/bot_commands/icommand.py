from telegram import Update
from telegram.ext import CallbackContext


from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    async def execute(self, update: Update, context: CallbackContext) -> None:
        pass