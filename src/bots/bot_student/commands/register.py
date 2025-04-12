from ..States.RegisterStates import RegisterStates


from aiogram.types import ReplyKeyboardRemove


async def register(message, state):
    await message.answer(
        "👤 Por favor, ingresa tu *nombre*:",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(RegisterStates.first_name)