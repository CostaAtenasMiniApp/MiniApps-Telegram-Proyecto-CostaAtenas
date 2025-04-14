# --- Flujo de Registro ---
from ..States.RegisterStates import RegisterStates
from ..commands.register import register
from ..process.register.first_name import first_name
from ..process.register.last_name import last_name
from ..process.register.process_email_registration import process_email_registration
from ..process.register.register_user_in_db import register_student_in_db
from src.core.services import StudentService, CourseService

from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


async def register_register_commands(student_service: StudentService
                                    , course_service: CourseService
                                    , dp: Dispatcher):
    @dp.message(Command("register"))
    async def cmd_register(message: types.Message, state: FSMContext):
        await register(message, state)

    @dp.message(RegisterStates.first_name)
    async def process_first_name(message: types.Message, state: FSMContext):
        return await first_name(message, state)

    @dp.message(RegisterStates.last_name)
    async def process_last_name(message: types.Message, state: FSMContext):
        return await last_name(message, state)

    @dp.message(RegisterStates.email)
    async def process_email(message: types.Message, state: FSMContext):
        await process_email_registration(student_service, course_service, message, state)

    @dp.message(RegisterStates.course)
    async def process_course(message: types.Message, state: FSMContext):
        await register_student_in_db(student_service,message, state)