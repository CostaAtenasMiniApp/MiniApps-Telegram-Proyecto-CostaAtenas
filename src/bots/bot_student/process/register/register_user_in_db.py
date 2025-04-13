from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove


import sqlite3


async def register_user_in_db(connection, message: types.Message, state: FSMContext):
    course_name = message.text
    user_data = await state.get_data()

    telegram_id = message.from_user.id
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    email = user_data['email']

    answer_message = insert_student(connection, course_name,
                            telegram_id,
                            first_name,
                            last_name,
                            email)

    await message.answer(
        answer_message,
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


def insert_student(connection, course_name:str,
                telegram_id:int, first_name:str, last_name:str, email):

    # Guardar en la base de datos
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (user_id, first_name, last_name, email) VALUES (?, ?, ?, ?)",
            (telegram_id, first_name, last_name, email)
        )
        connection.commit()
    except sqlite3.IntegrityError:
        answer_message = "❌ Error: Ya estás registrado."
    finally:
        connection.close()

    answer_message = (
        f"✅ *Registro completado* ✅\n\n"
        f"• Nombre: {first_name} {last_name}\n"
        f"• Email: {email}\n"
        f"• Curso: {course_name}"
    )
    return answer_message