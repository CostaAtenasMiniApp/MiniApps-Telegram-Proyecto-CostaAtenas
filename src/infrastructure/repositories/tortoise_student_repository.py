from datetime import date
from typing import List, Optional
from src.core.ports.istudent_repository import IStudentRepository
from src.core.domain import StudentDomain, Enrollment
from src.infrastructure.database.tortoise.models import Student
from tortoise import fields, models
from tortoise.transactions import in_transaction


class TortoiseStudentRepository(IStudentRepository):
    async def save(self, student: StudentDomain) -> int:
        """
        Guarda un estudiante en la base de datos.
        Retorna el student_id del estudiante guardado.
        """
        async with in_transaction():
            student_model, created = await Student.get_or_create(
                student_id=student.student_id,
                defaults={
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "email": student.email,
                    "registration_date": student.registration_date
                }
            )

            if not created:
                student_model.first_name = student.first_name
                student_model.last_name = student.last_name
                student_model.email = student.email
                student_model.registration_date = student.registration_date
                await student_model.save()

            # Aquí deberías manejar las enrollments si es necesario
            # Por ejemplo:
            # await self._process_enrollments(student_model, student.enrollments)

            return student_model.student_id

    async def find_by_id(self, student_id: int) -> Optional[StudentDomain]:
        """Busca un estudiante por ID. Retorna None si no existe."""
        student_model = await Student.get_or_none(student_id=student_id)
        if not student_model:
            return None

        # Aquí deberías cargar las enrollments si es necesario
        # Por ejemplo:
        # enrollments = await self._get_enrollments_for_student(student_model)

        return StudentDomain(
            student_id=student_model.student_id,
            first_name=student_model.first_name,
            last_name=student_model.last_name,
            email=student_model.email,
            registration_date=student_model.registration_date,
            enrollments=[]  # Reemplazar con las enrollments cargadas
        )

    async def find_all(self) -> List[StudentDomain]:
        """Retorna todos los estudiantes en la base de datos."""
        student_models = await Student.all()
        students = []

        for model in student_models:
            # Cargar enrollments para cada estudiante si es necesario
            students.append(StudentDomain(
                student_id=model.student_id,
                first_name=model.first_name,
                last_name=model.last_name,
                email=model.email,
                registration_date=model.registration_date,
                enrollments=[]  # Reemplazar con enrollments cargadas
            ))

        return students

    async def delete(self, student_id: int) -> None:
        """Elimina un estudiante por ID."""
        async with in_transaction():
            student_model = await Student.get_or_none(student_id=student_id)
            if student_model:
                # Primero eliminar enrollments relacionadas si es necesario
                # await EnrollmentModel.filter(student_id=student_id).delete()
                await student_model.delete()

    # Métodos auxiliares para manejar enrollments (ejemplo)
    async def _get_enrollments_for_student(self, student_model: Student) -> List[Enrollment]:
        """
        Ejemplo de cómo cargar enrollments relacionadas.
        Necesitarías tener un EnrollmentModel y convertir a objetos Enrollment del dominio.
        """
        # from infrastructure.database.tortoise.models import Enrollment as EnrollmentModel
        # enrollment_models = await EnrollmentModel.filter(student=student_model).all()
        # return [Enrollment(...) for e in enrollment_models]
        return []

    async def _process_enrollments(self, student_model: Student, enrollments: List[Enrollment]):
        """
        Ejemplo de cómo procesar enrollments al guardar un estudiante.
        """
        # from infrastructure.database.tortoise.models import Enrollment as EnrollmentModel
        # await EnrollmentModel.filter(student=student_model).delete()
        # for enrollment in enrollments:
        #     await EnrollmentModel.create(
        #         student=student_model,
        #         course_id=enrollment.course_id,
        #         enrollment_date=enrollment.enrollment_date,
        #         # otros campos
        #     )
        pass