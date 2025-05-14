from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove
import asyncio

import os
from dotenv import load_dotenv
from src.core.services import StudentService, CourseService
from src.infrastructure.repositories import TortoiseStudentRepository, TortoiseCourseRepository
from src.infrastructure.database.tortoise_db_models.init_db import init_db

from .register_commads import (
    register_additional_commands,
    register_basic_commands,
    register_course_commands,
    register_register_commands,
)

# Configuración inicial
load_dotenv()
student_token = os.getenv("StudentCifPlayasBot")
bot = Bot(token=student_token)
dp = Dispatcher()

# --- Cancelar cualquier flujo ---
@dp.message(Command("cancel"))
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Operación cancelada.", reply_markup=ReplyKeyboardRemove())

# --- Ejecutar el bot ---
async def main():
    await init_db()

    # Inicializa el repositorio de student y el servicio de student
    student_repository = TortoiseStudentRepository()
    student_service = StudentService(student_repository)

    # Inicializa el repositorio de cursos y el servicio de cursos
    course_repository = TortoiseCourseRepository()
    course_service = CourseService(course_repository)

    await register_basic_commands(dp)
    await register_register_commands(student_service, course_service, dp)
    await register_course_commands(dp)
    await register_additional_commands(dp)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())