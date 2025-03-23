from .academic_coordinator import AcademicCoordinator
from .professor import Professor
from .module import Module
from .enrollment import Enrollment
from .evaluation import Evaluation
from datetime import date

class Course:
    def __init__(
        self,
        id_course: int,
        name: str,
        description: str,
        start_date: date,
        end_date: date,
        status: str,
        academic_coordinator: AcademicCoordinator,
        professors: list[Professor],
        modules: list[Module],
        enrollments: list[Enrollment],
        evaluations: list[Evaluation]
    ):
        self.id_course = id_course
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.academic_coordinator = academic_coordinator
        self.professors = professors
        self.modules = modules
        self.enrollments = enrollments
        self.evaluations = evaluations