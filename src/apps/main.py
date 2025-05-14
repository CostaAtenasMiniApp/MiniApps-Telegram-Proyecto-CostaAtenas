from flask import Flask
from src.apps.routes import register_routes  # Cambiado a import absoluto
from src.core.services import StudentService
from src.infrastructure.repositories import TortoiseStudentRepository
from src.infrastructure.database.tortoise_db_models.init_db import init_db
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='template')
app.secret_key = os.getenv('FLASK_SECRET_KEY', '18d8791438b46514da6b131e360a2392')

# Estado de inicialización
_initialized = False

async def initialize_app():
    """Función de inicialización separada"""
    global _initialized
    if not _initialized:
        await init_db()
        student_repository = TortoiseStudentRepository()
        student_service = StudentService(student_repository)
        register_routes(app, student_service)
        _initialized = True

def create_app():
    """Factory para WSGI que no ejecuta asyncio.run()"""
    return app

if __name__ == "__main__":
    import asyncio
    asyncio.run(initialize_app())
    app.run(debug=True)