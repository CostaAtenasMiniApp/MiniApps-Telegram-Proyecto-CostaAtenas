async def lesson(message, state):
    if not message.text.isdigit():
        await message.answer("❌ Debe ser un número. Intenta de nuevo.")
        return

    lesson = int(message.text)
    user_data = await state.get_data()

    await message.answer(
        f"🔍 *Curso encontrado* 🔍\n\n"
        f"• Curso: {user_data['course_number']}\n"
        f"• Lección: {lesson}\n\n"
        f"📂 Contenido disponible: [Ver material](#)",
        parse_mode="Markdown"
    )
    await state.clear()