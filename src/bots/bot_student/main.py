from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import re
import sqlite3
import asyncio
from aiogram.types import ReplyKeyboardRemove

import os
from dotenv import load_dotenv

from .commands.help import help
from .commands.forum import forum
from .commands.grades import grades
from .commands.my_courses import my_courses
from .commands.progress import progress
from .commands.submit_task import submit_task
from .commands.view_content import view_content

from .States.CourseStates import CourseStates
from .States.RegisterStates import RegisterStates
from .commands.start import start

# Configuración inicial
load_dotenv()
student_token = os.getenv("StudientCifPlayasBot")
bot = Bot(token=student_token)
dp = Dispatcher()

# --- Base de datos SQLite ---
def init_db():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE
    )''')
    
    # Tabla de cursos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )''')
    
    conn.commit()
    conn.close()

init_db()

# --- Comandos básicos ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await start(message)

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await help(message)

# --- Flujo de Registro ---
@dp.message(Command("register"))
async def cmd_register(message: types.Message, state: FSMContext):
    await message.answer(
        "👤 Por favor, ingresa tu *nombre*:",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(RegisterStates.first_name)

@dp.message(RegisterStates.first_name)
async def process_first_name(message: types.Message, state: FSMContext):
    return await first_name(message, state)

async def first_name(message, state):
    if not message.text or len(message.text) > 50:
        await message.answer("❌ Nombre inválido. Máximo 50 caracteres.")
        return
    
    await state.update_data(first_name=message.text)
    await message.answer("👥 Ahora ingresa tu *apellido*:")
    await state.set_state(RegisterStates.last_name)

@dp.message(RegisterStates.last_name)
async def process_last_name(message: types.Message, state: FSMContext):
    return await last_name(message, state)

async def last_name(message, state):
    if not message.text or len(message.text) > 50:
        await message.answer("❌ Apellido inválido. Máximo 50 caracteres.")
        return
    
    await state.update_data(last_name=message.text)
    await message.answer("📧 Ingresa tu *email* (ejemplo: usuario@dominio.com):")
    await state.set_state(RegisterStates.email)

@dp.message(RegisterStates.email)
async def process_email(message: types.Message, state: FSMContext):
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

@dp.message(RegisterStates.course)
async def process_course(message: types.Message, state: FSMContext):
    course_name = message.text
    user_data = await state.get_data()
    
    # Guardar en la base de datos
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO users (user_id, first_name, last_name, email) VALUES (?, ?, ?, ?)",
            (message.from_user.id, user_data['first_name'], user_data['last_name'], user_data['email'])
        )
        conn.commit()
    except sqlite3.IntegrityError:
        await message.answer("❌ Error: Ya estás registrado.")
    finally:
        conn.close()
    
    await message.answer(
        f"✅ *Registro completado* ✅\n\n"
        f"• Nombre: {user_data['first_name']} {user_data['last_name']}\n"
        f"• Email: {user_data['email']}\n"
        f"• Curso: {course_name}",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()

# --- Comando /damecurso ---
@dp.message(Command("damecurso"))
async def cmd_get_course(message: types.Message, state: FSMContext):
    await message.answer(
        "📚 Ingresa el *número del curso* que deseas buscar:",
        parse_mode="Markdown"
    )
    await state.set_state(CourseStates.course_number)

@dp.message(CourseStates.course_number)
async def process_course_number(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Debe ser un número. Intenta de nuevo.")
        return
    
    course_number = int(message.text)
    await state.update_data(course_number=course_number)
    await message.answer("📖 Ahora ingresa el *número de lección*:")
    await state.set_state(CourseStates.lesson)

@dp.message(CourseStates.lesson)
async def process_lesson(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Debe ser un número. Intenta de nuevo.")
        return
    
    lesson = int(message.text)
    user_data = await state.get_data()
    
    await message.answer(
        f"🔍 *Curso encontrado* 🔍\n\n"
        f"• Curso: {user_data['course_number']}\n"
        f"• Lección: {lesson}\n\n"
        f"📂 Contenido disponible: [Ver material](#)",
        parse_mode="Markdown"
    )
    await state.clear()

# --- Comandos adicionales ---
@dp.message(Command("mycourses"))
async def cmd_mycourses(message: types.Message):
    # Lógica para obtener cursos del usuario
    await my_courses(message)

@dp.message(Command("viewcontent"))
async def cmd_viewcontent(message: types.Message):
    await view_content(message)

@dp.message(Command("submittask"))
async def cmd_submittask(message: types.Message):
    await submit_task(message)

@dp.message(Command("grades"))
async def cmd_grades(message: types.Message):
    await grades(message)

@dp.message(Command("forum"))
async def cmd_forum(message: types.Message):
    await forum(message)

@dp.message(Command("progress"))
async def cmd_progress(message: types.Message):
    await progress(message)

# --- Cancelar cualquier flujo ---
@dp.message(Command("cancel"))
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Operación cancelada.", reply_markup=ReplyKeyboardRemove())

# --- Ejecutar el bot ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())