from .enrollment import Enrollment
from datetime import date

class Student:
    def __init__(
        self,
        student_id: int,
        first_name: str,
        last_name: str,
        email: str,
        registration_date: date,
        enrollments: list[Enrollment]
    ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollments = enrollments
        self.registration_date = registration_date