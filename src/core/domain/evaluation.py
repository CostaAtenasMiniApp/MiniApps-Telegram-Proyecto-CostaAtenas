from .course import Course
from .module import Module
from datetime import date

class Evaluation:
    def __init__(
        self,
        id_evaluation: int,
        title: str,
        description: str,
        deadline: date,
        course: Course,
        module: Module
    ):
        self.id_evaluation = id_evaluation
        self.title = title
        self.description = description
        self.deadline = deadline
        self.course = course
        self.module = module