from datetime import date
from typing import List, Optional
from src.core.ports.istudent_repository import IStudentRepository
from src.core.domain import StudentDomain, Enrollment
from src.infrastructure.database.tortoise.models import Student
from tortoise.transactions import in_transaction


class TortoiseStudentRepository(IStudentRepository):
    async def save(self, student: StudentDomain) -> int:
        """
        Guarda un estudiante en la base de datos.
        Retorna el student_id del estudiante guardado.
        """
        async with in_transaction():
            student_data = {
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "national_id": student.national_id,
                "phone": student.phone,
                "country": student.country,
                "city": student.city,
                "is_proplayas_member": student.is_proplayas_member,
                "proplayas_node": student.proplayas_node,
                "belongs_to_hotel": student.belongs_to_hotel,
                "hotel_name": student.hotel_name,
                "age": student.age,
                "other_discovery_info": student.other_discovery_info,
                "referral_info": student.referral_info,
                "education_level": student.education_level,
                "study_area": student.study_area,
                "work_area": student.work_area,
                "course_motivation": student.course_motivation,
                "wants_certification_info": student.wants_certification_info,
                "registration_date": student.registration_date
            }

            if student.student_id is None:
                # Crear nuevo estudiante
                student_model = await Student.create(**student_data)
            else:
                # Actualizar estudiante existente
                student_model = await Student.get(student_id=student.student_id)
                await student_model.update_from_dict(student_data).save()

            # Manejar métodos de descubrimiento (relación ManyToMany)
            if student.discovery_methods:
                await student_model.discovery_methods.clear()
                await student_model.discovery_methods.add(*student.discovery_methods)

            # Manejar beca (relación ForeignKey)
            if hasattr(student, 'scholarship') and student.scholarship:
                student_model.scholarship = student.scholarship
                await student_model.save()

            return student_model.student_id

    async def find_by_id(self, student_id: int) -> Optional[StudentDomain]:
        """Busca un estudiante por ID. Retorna None si no existe."""
        student_model = await Student.get_or_none(student_id=student_id)
        if not student_model:
            return None

        # Aquí deberías cargar las enrollments si es necesario
        # Por ejemplo:
        # enrollments = await self._get_enrollments_for_student(student_model)

        return StudentDomain.from_model(student_model)



    async def find_all(self) -> List[StudentDomain]:
        """Retorna todos los estudiantes en la base de datos."""
        student_models = await Student.all()
        students = []

        for model in student_models:
            students.append(StudentDomain(
                student_id=model.student_id,
                first_name=model.first_name,
                last_name=model.last_name,
                email=model.email,
                national_id=model.national_id,
                phone=model.phone,
                country=model.country,
                city=model.city,
                is_proplayas_member=model.is_proplayas_member,
                proplayas_node=model.proplayas_node,
                belongs_to_hotel=model.belongs_to_hotel,
                hotel_name=model.hotel_name,
                age=model.age,
                other_discovery_info=model.other_discovery_info,
                referral_info=model.referral_info,
                education_level=model.education_level,
                study_area=model.study_area,
                work_area=model.work_area,
                course_motivation=model.course_motivation,
                wants_certification_info=model.wants_certification_info,
                registration_date=model.registration_date
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