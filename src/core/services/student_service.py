# core/services/user_service.py
from core.ports.istudent_repository import IStudentRepository
from core.domain.student import Student

class StudentService:
    def __init__(self, student_repository: IStudentRepository):
        self.student_repository = student_repository

    def register_student(self, name: str, email: str) -> Student:
        student = Student(id="123", first_name=name, email=email)
        self.student_repository.save(student)
        return student