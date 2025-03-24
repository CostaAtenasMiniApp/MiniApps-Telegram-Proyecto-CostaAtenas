from flask import Flask, render_template, request, jsonify
from EcecuteCommandBot import EcecuteCommandBot

app = Flask(__name__, template_folder='template')

@app.route('/classroom')
def classroom():
    return render_template('miniapp_classroom/index.html')

@app.route('/professor')
def professor():
    return render_template('miniapp_professor/index.html')

# Token del bot (guardado en una variable de entorno en producción)
@app.route('/execute-command', methods=['POST'])
def execute_command():
    command_bot = EcecuteCommandBot(request.json)
    if command_bot.is_data_missing():
        return {'error': 'Missing data'}, 400
    result, status_code = command_bot.send_command_to_bot()
    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(debug=True)
