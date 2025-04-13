from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
import sqlite3
import asyncio
from aiogram.types import ReplyKeyboardRemove

import os
from dotenv import load_dotenv

from .router.register_additional_commands import register_additional_commands
from .router.register_basic_commands import register_basic_commands
from .router.register_course_commands import register_course_commands
from .router.register_register_commands import register_register_commands

from  ...infrastructure.database.sqlite import  init_db

# Configuración inicial
load_dotenv()
student_token = os.getenv("StudientCifPlayasBot")
bot = Bot(token=student_token)
dp = Dispatcher()

# --- Base de datos SQLite ---
init_db()
connection = sqlite3.connect('courses.db')

# --- Cancelar cualquier flujo ---
@dp.message(Command("cancel"))
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Operación cancelada.", reply_markup=ReplyKeyboardRemove())

# --- Ejecutar el bot ---
async def main():
    await register_basic_commands(dp)
    await register_register_commands(connection, dp)
    await register_course_commands(dp)
    await register_additional_commands(dp)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())