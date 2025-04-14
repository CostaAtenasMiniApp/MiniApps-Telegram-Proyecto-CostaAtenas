from datetime import date
from typing import List, Optional
from src.core.ports.icourse_repository import ICourseRepository
from src.core.domain import CourseDomain
from src.infrastructure.database.tortoise.models import Course
from tortoise import fields, models
from tortoise.transactions import in_transaction


class TortoiseCourseRepository(ICourseRepository):
    async def save(self, course: CourseDomain) -> int:
        """
        Guarda un curso en la base de datos.
        Retorna el id_course del curso guardado.
        """
        async with in_transaction():
            course_model, created = await Course.get_or_create(
                id_course=course.id_course,
                defaults={
                    "name": course.name,
                    "description": course.description,
                    "start_date": course.start_date,
                    "duration": course.duration,
                    "status": course.status
                }
            )

            if not created:
                course_model.name = course.name
                course_model.description = course.description
                course_model.start_date = course.start_date
                course_model.duration = course.duration
                course_model.status = course.status
                await course_model.save()

            return course_model.id_course

    async def find_by_id(self, id_course: int) -> Optional[CourseDomain]:
        """Busca un curso por ID. Retorna None si no existe."""
        course_model = await Course.get_or_none(id_course=id_course)
        if not course_model:
            return None

        return CourseDomain(
            id_course=course_model.id_course,
            name=course_model.name,
            description=course_model.description,
            start_date=course_model.start_date,
            duration=course_model.duration,
            status=course_model.status
        )

    async def find_all(self) -> List[CourseDomain]:
        """Retorna todos los cursos en la base de datos."""
        course_models = await Course.all()
        courses = []

        for model in course_models:
            courses.append(CourseDomain(
                id_course=model.course_id,
                name=model.name,
                description=model.description,
                start_date=model.start_date,
                duration=model.duration,
                status=model.status
            ))

        return courses

    async def delete(self, id_course: int) -> None:
        """Elimina un curso por ID."""
        async with in_transaction():
            course_model = await Course.get_or_none(course_id=id_course)
            if course_model:
                await course_model.delete()
