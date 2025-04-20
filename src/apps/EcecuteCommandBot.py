from flask import jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar las variables de entorno desde un archivo .env

class EcecuteCommandBot:
    def __init__(self, data):
        self.chat_id = data.get('chat_id')
        self.command = data.get('command')
        self.bot_name = data.get('bot')

    def is_data_missing(self):
        if not self.chat_id or not self.command or not self.bot_name:
            return True

    def get_bot_token(self):
        match self.bot_name:
            case 'bot_classroom':
                BOT_TOKEN = os.getenv('BOT_TOKEN_CLASSROOM')
            case 'bot_professor':
                BOT_TOKEN = os.getenv('BOT_TOKEN_PROFESSOR')
            case _:
                return ""
        return BOT_TOKEN

    def send_command_to_bot(self):
        # Send the command to the bot using the Telegram API
        BOT_TOKEN = self.get_bot_token()
        if not BOT_TOKEN:
            return jsonify({'error': 'Bot no reconocido'}), 400
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        payload = {
            'chat_id': self.chat_id,
            'text': self.command
        }
        response = requests.post(url, json=payload)
        return {'success': response.status_code == 200}, response.status_code