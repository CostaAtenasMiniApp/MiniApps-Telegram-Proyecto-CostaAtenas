from ...States.RegisterStates import RegisterStates


async def first_name(message, state):
    if not message.text or len(message.text) > 50:
        await message.answer("❌ Nombre inválido. Máximo 50 caracteres.")
        return

    await state.update_data(first_name=message.text)
    await message.answer("👥 Ahora ingresa tu *apellido*:")
    await state.set_state(RegisterStates.last_name)