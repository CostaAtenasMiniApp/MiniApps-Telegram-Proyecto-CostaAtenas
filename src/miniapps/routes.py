from flask import render_template, request, jsonify
from EcecuteCommandBot import EcecuteCommandBot

def register_routes(app):
    @app.route('/classroom')
    def classroom():
        return render_template('miniapp_classroom/index.html')

    @app.route('/professor')
    def professor():
        return render_template('miniapp_professor/index.html')

    @app.route('/execute-command', methods=['POST'])
    def execute_command():
        command_bot = EcecuteCommandBot(request.json)
        if command_bot.is_data_missing():
            return {'error': 'Missing data'}, 400
        result, status_code = command_bot.send_command_to_bot()
        return jsonify(result), status_code
