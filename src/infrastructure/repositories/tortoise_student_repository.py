from src.core.ports.istudent_repository import IStudentRepository
from  core.domain import Student as StudentDomain
from infrastructure.database.tortoise.models import Student as StudentModel

class TortoiseStudentRepository(IStudentRepository):
    async def save(self, student: StudentDomain) -> None:
        await StudentModel.create(
            student_id=student.student_id,
            first_name=student.first_name,
            last_name=student.last_name,
            email=student.email
        )

    async def find_by_id(self, student_id: str) -> StudentDomain | None:
        student_record = await StudentModel.filter(student_id=student_id).first()
        if student_record:
            return StudentDomain(
                student_id=student_record.student_id,
                first_name=student_record.first_name,
                last_name=student_record.last_name,
                email=student_record.email
            )
        return None