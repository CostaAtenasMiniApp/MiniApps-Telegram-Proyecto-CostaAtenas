from ...States.RegisterStates import RegisterStates


async def last_name(message, state):
    if not message.text or len(message.text) > 50:
        await message.answer("❌ Apellido inválido. Máximo 50 caracteres.")
        return

    await state.update_data(last_name=message.text)
    await message.answer("📧 Ingresa tu *email* (ejemplo: usuario@dominio.com):")
    await state.set_state(RegisterStates.email)