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
    ):
        self.id_course = id_course
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status