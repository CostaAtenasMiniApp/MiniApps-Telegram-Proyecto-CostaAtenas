class MyTelegramBot(TelegramBotTemplate):
    def start_command(self, message: types.Message) -> None:
        welcome_text = (
            "¡Bienvenido al bot!\n"
            "Usa /help para ver los comandos disponibles."
        )
        self.bot.reply_to(message, welcome_text)

    def help_command(self, message: types.Message) -> None:
        help_text = (
            "Comandos disponibles:\n"
            "/start - Inicia el bot\n"
            "/help - Muestra esta ayuda"
        )
        self.bot.reply_to(message, help_text)

    def handle_text(self, message: types.Message) -> None:
        if message.text.lower() == "hola":
            self.bot.reply_to(message, "¡Hola! ¿Cómo estás?")
        else:
            self.bot.reply_to(message, f"Recibí: {message.text}")

    def handle_photo(self, message: types.Message) -> None:
        self.bot.reply_to(message, "¡Foto recibida! 📸")

    def setup_handlers(self) -> None:
        # Comandos
        self.bot.message_handler(commands=['start'])(self.start_command)
        self.bot.message_handler(commands=['help'])(self.help_command)
        
        # Contenido
        self.bot.message_handler(content_types=['text'])(self.handle_text)
        self.bot.message_handler(content_types=['photo'])(self.handle_photo)

    def run(self) -> None:
        self.setup_handlers()
        print("Bot en ejecución...")
        self.bot.polling(none_stop=True)


if __name__ == "__main__":
    bot = MyTelegramBot("TU_TOKEN_AQUI")
    bot.run()
