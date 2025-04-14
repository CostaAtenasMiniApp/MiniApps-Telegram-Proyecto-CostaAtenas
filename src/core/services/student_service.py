# core/services/user_service.py
from src.core.ports.istudent_repository import IStudentRepository
from src.core.domain.student_domain import StudentDomain

class StudentService:
    def __init__(self, student_repository: IStudentRepository):
        self.student_repository = student_repository

    async def create_student(self, student) -> StudentDomain:
        await self.student_repository.save(student)
        return student

    async def get_student_by_id(self, student_id: int) -> StudentDomain:
        return await self.student_repository.find_by_id(student_id)

    async def get_all_students(self) -> list[StudentDomain]:
        return await self.student_repository.find_all()

    async def update_student(self, student_id: int, first_name: str = None,
                            last_name: str = None,
                            email: str = None) -> StudentDomain:
        student = await self.student_repository.find_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if email:
            student.email = email
        await self.student_repository.save(student)
        return student

    async def delete_student(self, student_id: int) -> None:
        student = await self.student_repository.find_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        await self.student_repository.delete(student_id)