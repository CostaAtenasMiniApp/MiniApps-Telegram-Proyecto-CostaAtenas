from ...States.RegisterStates import RegisterStates


from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


import re
import sqlite3


async def process_email_registration(message: types.Message, state: FSMContext):
    email = message.text.strip()
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        await message.answer("❌ Email inválido. Intenta de nuevo.")
        return

    # Verificar si el email ya existe
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
    if cursor.fetchone():
        await message.answer("❌ Este email ya está registrado.")
        conn.close()
        return

    await state.update_data(email=email)

    # Mostrar cursos disponibles
    cursor.execute("SELECT name FROM courses")
    courses = cursor.fetchall()
    conn.close()

    if not courses:
        await message.answer("No hay cursos disponibles actualmente.")
        await state.clear()
        return

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=course[0])] for course in courses],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(
        "📚 Selecciona el curso al que deseas inscribirte:",
        reply_markup=keyboard
    )
    await state.set_state(RegisterStates.course)