# --- Estados para /damecurso ---
from aiogram.fsm.state import State, StatesGroup


class CourseStates(StatesGroup):
    course_number = State()
    lesson = State()