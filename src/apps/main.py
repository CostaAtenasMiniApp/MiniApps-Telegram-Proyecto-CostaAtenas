from flask import Flask
from .routes import register_routes
import asyncio

from src.core.services import StudentService
from src.infrastructure.repositories import TortoiseStudentRepository
from src.infrastructure.database.tortoise.init_db import init_db

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='template')
app.secret_key = os.getenv('FLASK_SECRET_KEY', '18d8791438b46514da6b131e360a2392')

# Mueve la inicialización a una función aparte
async def init_app():
    await init_db()
    student_repository = TortoiseStudentRepository()
    student_service = StudentService(student_repository)
    register_routes(app, student_service)

# Esto asegura que `app` esté disponible para PythonAnywhere
if __name__ == "__main__":
    asyncio.run(init_app())
    app.run(debug=True)