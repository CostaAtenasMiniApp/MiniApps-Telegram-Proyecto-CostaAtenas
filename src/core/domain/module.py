from .course import Course

class Module:
    def __init__(
        self,
        id_module: int,
        name: str,
        description: str,
        order: int,
        course: Course,
    ):
        self.id_module = id_module
        self.name = name
        self.description = description
        self.order = order
        self.course = course