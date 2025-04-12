from src.infrastructure.database.models import Student

class StudentRepository:
    async def get_student_by_id(self, student_id: int):
        return await Student.filter(student_id=student_id).first()

    async def create_student(self, name: str, email: str):
        return await Student.create(name=name, email=email)

    async def list_students(self):
        return await Student.all()