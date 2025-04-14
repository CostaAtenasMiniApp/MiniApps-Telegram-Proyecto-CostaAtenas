from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from src.core.services import StudentService
from src.core.domain import StudentDomain

from datetime import datetime


async def register_student_in_db(student_service: StudentService, message: types.Message, state: FSMContext):
    course_name = message.text
    user_data = await state.get_data()

    telegram_id = message.from_user.id
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    email = user_data['email']

    student = StudentDomain(
        student_id=telegram_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        registration_date=datetime.now()
    )

    try:
        await student_service.create_student(student)
        answer_message = (
            f"✅ *Registro completado* ✅\n\n"
            f"• Nombre: {first_name} {last_name}\n"
            f"• Email: {email}\n"
            f"• Curso: {course_name}"
        )
    except Exception as e:
        answer_message = f"❌ Error al registrar al usuario: {str(e)}"

    await message.answer(
        answer_message,
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()
