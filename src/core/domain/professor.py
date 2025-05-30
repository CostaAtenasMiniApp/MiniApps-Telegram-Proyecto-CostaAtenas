from .course import CourseDomain

class Professor:
    def __init__(
        self,
        id_professor: int,
        name: str,
        email: str,
        specialty: str,
        courses: list[CourseDomain]
    ):
        self.id_professor = id_professor
        self.name = name
        self.email = email
        self.specialty = specialty
        self.courses = courses