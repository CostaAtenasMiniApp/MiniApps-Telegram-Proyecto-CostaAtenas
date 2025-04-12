# --- Estados para el registro ---
from aiogram.fsm.state import State, StatesGroup


class RegisterStates(StatesGroup):
    first_name = State()
    last_name = State()
    email = State()
    course = State()