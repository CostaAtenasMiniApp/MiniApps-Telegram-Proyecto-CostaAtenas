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

_initialized = False

async def initialize_app():
    global _initialized
    if not _initialized:
        await init_db()
        student_repository = TortoiseStudentRepository()
        student_service = StudentService(student_repository)
        register_routes(app, student_service)
        _initialized = True

def create_app():
    """Factory para WSGI que inicializa todo antes de devolver app"""
    global _initialized
    print("Entrando a create_app", flush=True)
    if not _initialized:
        import asyncio
        try:
            print("Inicializando app async...", flush=True)
            asyncio.run(initialize_app())
            print("Inicialización async completada", flush=True)
        except Exception as e:
            print("Error durante la inicialización:", e, flush=True)
            raise
    else:
        print("App ya inicializada", flush=True)
    return app

if __name__ == "__main__":
    import asyncio
    asyncio.run(initialize_app())
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)