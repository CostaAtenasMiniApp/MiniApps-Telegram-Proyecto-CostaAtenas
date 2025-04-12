from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove


import sqlite3


async def register_user_in_db(message: types.Message, state: FSMContext):
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