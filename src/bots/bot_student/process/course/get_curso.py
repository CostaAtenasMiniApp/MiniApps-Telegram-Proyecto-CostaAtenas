from ...States.CourseStates import CourseStates


async def get_curso(message, state):
    await message.answer(
        "📚 Ingresa el *número del curso* que deseas buscar:",
        parse_mode="Markdown"
    )
    await state.set_state(CourseStates.course_number)