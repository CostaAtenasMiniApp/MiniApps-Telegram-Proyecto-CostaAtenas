from .student_domain import StudentDomain
from .course import CourseDomain
from datetime import date

class Enrollment:
    def __init__(
        self,
        id_enrollment: int,
        enrollment_date: date,
        status: str,
        graduation_date: date,
        student: StudentDomain,
        course: CourseDomain
    ):
        self.id_enrollment = id_enrollment
        self.enrollment_date = enrollment_date
        self.status = status
        self.graduation_date = graduation_date
        self.student = student
        self.course = course