from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv


load_dotenv()  # Cargar las variables de entorno desde un archivo .env

app = Flask(__name__, template_folder='template')

@app.route('/classroom')
def classroom():
    return render_template('miniapp_classroom/index.html')

@app.route('/professor')
def professor():
    return render_template('miniapp_professor/index.html')

# Token del bot (guárdalo en una variable de entorno en producción)

@app.route('/execute-command', methods=['POST'])
def execute_command():
    data = request.json
    chat_id = data.get('chat_id')
    command = data.get('command')
    bot_name = data.get('bot')

    match bot_name:
        case 'bot_classroom':
            BOT_TOKEN = os.getenv('BOT_TOKEN_CLASSROOM')
        case 'bot_professor':
            BOT_TOKEN = os.getenv('BOT_TOKEN_PROFESSOR')
        case _:
            return jsonify({'error': 'Bot no reconocido'}), 400

    if not chat_id or not command:
        return {'error': 'Missing data'}, 400

    result, status_code = send_command_to_bot(BOT_TOKEN, chat_id, command)
    return jsonify(result), status_code

def send_command_to_bot(bot_token, chat_id, command):
    # Send the command to the bot using the Telegram API
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': command
    }
    response = requests.post(url, json=payload)
    return {'success': response.status_code == 200}, response.status_code

if __name__ == '__main__':
    app.run(debug=True)
