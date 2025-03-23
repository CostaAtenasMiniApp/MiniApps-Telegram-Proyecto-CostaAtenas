from .course import Course
from .lesson import Lesson
from .evaluation import Evaluation

class Module:
    def __init__(
        self,
        id_module: int,
        name: str,
        description: str,
        order: int,
        course: Course,
        lessons: list[Lesson],
        evaluations: list[Evaluation]
    ):
        self.id_module = id_module
        self.name = name
        self.description = description
        self.order = order
        self.course = course
        self.lessons = lessons
        self.evaluations = evaluations