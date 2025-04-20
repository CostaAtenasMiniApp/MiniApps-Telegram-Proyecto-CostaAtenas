from flask import Flask
from .routes import register_routes
import asyncio

from src.core.services import StudentService
from src.infrastructure.repositories import TortoiseStudentRepository
from src.infrastructure.database.tortoise.init_db import init_db


app = Flask(__name__, template_folder='template')

async def main():
    await init_db()
    # Inicializa el repositorio de student y el servicio de student
    student_repository = TortoiseStudentRepository()
    student_service = StudentService(student_repository)

    # Registrar las rutas desde el archivo separado
    register_routes(app, student_service)
    app.run(debug=True)


if __name__ == "__main__":
    asyncio.run(main())