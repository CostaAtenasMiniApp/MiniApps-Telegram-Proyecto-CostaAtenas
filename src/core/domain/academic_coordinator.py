from .course import CourseDomain

class AcademicCoordinator:
    def __init__(self, id_coordinator: int,
                name: str,
                email: str,
                phone: str,
                courses: list[CourseDomain]):
        self.id_coordinator = id_coordinator
        self.name = name
        self.email = email
        self.phone = phone
        self.courses = courses