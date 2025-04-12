# --- Comando /damecurso ---
from ..States.CourseStates import CourseStates
from ..process.course.course_number import course_number
from ..process.course.get_curso import get_curso
from ..process.course.lesson import lesson


from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


async def register_course_commands(dp: Dispatcher):
    @dp.message(Command("damecurso"))
    async def cmd_get_course(message: types.Message, state: FSMContext):
        await get_curso(message, state)

    @dp.message(CourseStates.course_number)
    async def process_course_number(message: types.Message, state: FSMContext):
        return await course_number(message, state)

    @dp.message(CourseStates.lesson)
    async def process_lesson(message: types.Message, state: FSMContext):
        return await lesson(message, state)