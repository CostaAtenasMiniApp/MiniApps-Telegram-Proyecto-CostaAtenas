# --- Comandos adicionales ---
from ..commands.forum import forum
from ..commands.grades import grades
from ..commands.my_courses import my_courses
from ..commands.progress import progress
from ..commands.submit_task import submit_task
from ..commands.view_content import view_content


from aiogram import Dispatcher, types
from aiogram.filters import Command


async def register_additional_commands(dp: Dispatcher):
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