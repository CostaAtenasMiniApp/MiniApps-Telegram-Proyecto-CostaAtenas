from .enrollment import Enrollment
from datetime import date

class Student:
    def __init__(
        self,
        id_student: int,
        name: str,
        email: str,
        registration_date: date,
        enrollments: list[Enrollment]
    ):
        self.id_student = id_student
        self.name = name
        self.email = email
        self.registration_date = registration_date
        self.enrollments = enrollments