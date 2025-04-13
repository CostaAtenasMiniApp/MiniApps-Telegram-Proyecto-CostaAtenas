from infrastructure.repositories.sqlite_student_repository import StudentRepository

class StudentUseCase:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    async def get_student(self, student_id: int):
        return await self.student_repository.get_student_by_id(student_id)

    async def register_student(self, name: str, email: str):
        return await self.student_repository.create_student(name, email)

    async def list_all_students(self):
        return await self.student_repository.list_students()