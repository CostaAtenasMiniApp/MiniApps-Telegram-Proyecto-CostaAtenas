from datetime import date

class CourseDomain:
    def __init__(
        self,
        id_course: int,
        name: str,
        description: str,
        start_date: date,
        duration: int,
        status: str,
    ):
        self.id_course = id_course
        self.name = name
        self.description = description
        self.start_date = start_date
        self.duration = duration
        self.status = status