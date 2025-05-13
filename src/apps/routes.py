from flask import render_template, request, jsonify, redirect, url_for, flash
from src.core.domain.student_domain import StudentDomain
from src.core.services import StudentService
from datetime import datetime

from .EcecuteCommandBot import EcecuteCommandBot

def register_routes(app, student_service: StudentService):
    @app.route('/', methods=['GET'])
    def landing_page():
        return render_template('miniapp_landing_page/index.html')

    @app.route('/student')
    def classroom():
        return render_template('miniapp_student/index.html')


    @app.route('/execute-command', methods=['POST'])
    def execute_command():
        command_bot = EcecuteCommandBot(request.json)
        if command_bot.is_data_missing():
            return {'error': 'Missing data'}, 400
        result, status_code = command_bot.send_command_to_bot()
        return jsonify(result), status_code

# Ruta para mostrar el formulario de registro e inscripción
    @app.route('/secciones/legal.html', methods=['GET'])
    def show_legal_form():
        return render_template('miniapp_registration/secciones/legal.html')

    @app.route('/secciones/identificacion.html', methods=['GET'])
    def show_identificacion_form():
        return render_template('miniapp_registration/secciones/identificacion.html')

    @app.route('/secciones/estadisticos.html', methods=['GET'])
    def show_estadisticos_form():
        return render_template('miniapp_registration/secciones/estadisticos.html')

    @app.route('/registration', methods=['GET'])
    def show_form():
        return render_template('miniapp_registration/index.html')

    # Ruta para procesar el formulario
    @app.route('/registration', methods=['POST'])
    async def process_form():
        form_data = request.form

        try:
            # Procesar métodos de descubrimiento (checkboxes)
            discovery_methods = request.form.getlist('discovery_method')

            # Crear instancia del estudiante SIN student_id para nuevo registro
            student = StudentDomain(
                registration_date=datetime.now(),
                email=form_data['email'],
                first_name=form_data['first_name'],
                last_name=form_data['last_name'],
                national_id=form_data.get('national_id'),
                phone=form_data.get('phone'),
                country=form_data.get('country'),
                city=form_data.get('city'),
                is_proplayas_member=form_data.get('is_proplayas_member') == 'true',
                proplayas_node=form_data.get('proplayas_node'),
                belongs_to_hotel=form_data.get('belongs_to_hotel') == 'true',
                hotel_name=form_data.get('hotel_name'),
                age=int(form_data['age']) if form_data.get('age') else None,
                discovery_methods=discovery_methods,
                other_discovery_info=form_data.get('other_discovery_info'),
                referral_info=form_data.get('referral_info'),
                scholarship_code=form_data.get('scholarship_code', 'No aplica'),
                education_level=form_data.get('education_level'),
                study_area=form_data.get('study_area'),
                work_area=form_data.get('work_area'),
                course_motivation=form_data.get('course_motivation'),
                wants_certification_info='wants_certification_info' in form_data
            )

            await student_service.create_student(student)

            flash('¡Registro exitoso! Gracias por inscribirte.', 'success')
            return redirect(url_for('show_form'))

        except Exception as e:
            flash(f'Error al procesar el formulario: {str(e)}', 'danger')
            return redirect(url_for('show_form'))

