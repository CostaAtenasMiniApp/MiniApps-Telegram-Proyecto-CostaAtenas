from ...States.RegisterStates import RegisterStates
from src.core.services import StudentService, CourseService

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import re


async def process_email_registration(student_service: StudentService
                                    , course_service: CourseService
                                    , message: types.Message, state: FSMContext):
    # Validar email
    email = message.text.strip()
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        await message.answer("❌ Email inválido. Intenta de nuevo.")
        return

    # Verificar si el email ya existe en Student usando StudentService
    existing_students = await student_service.get_all_students()
    if any(student.email == email for student in existing_students):
        await message.answer("❌ Este email ya está registrado.")
        return

    await state.update_data(email=email)

    # Validar que existan cursos
    courses = await course_service.get_all_course()
    if not courses:
        await message.answer("No hay cursos disponibles actualmente.")
        await state.clear()
        return

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=course.name)] for course in courses],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(
        "📚 Selecciona el curso al que deseas inscribirte:",
        reply_markup=keyboard
    )
    await state.set_state(RegisterStates.course)