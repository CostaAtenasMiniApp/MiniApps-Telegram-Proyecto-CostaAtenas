from ...States.CourseStates import CourseStates


async def course_number(message, state):
    if not message.text.isdigit():
        await message.answer("❌ Debe ser un número. Intenta de nuevo.")
        return

    course_number = int(message.text)
    await state.update_data(course_number=course_number)
    await message.answer("📖 Ahora ingresa el *número de lección*:")
    await state.set_state(CourseStates.lesson)