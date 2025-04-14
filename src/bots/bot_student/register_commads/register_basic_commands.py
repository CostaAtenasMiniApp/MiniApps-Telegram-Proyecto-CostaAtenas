# --- Comandos básicos ---
from ..commands.help import help
from ..commands.start import start


from aiogram import Dispatcher, types
from aiogram.filters import Command


async def register_basic_commands(dp: Dispatcher):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await start(message)

    @dp.message(Command("help"))
    async def cmd_help(message: types.Message):
        await help(message)