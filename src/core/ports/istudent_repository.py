from abc import ABC, abstractmethod
from ..domain.student import Student

class IStudentRepository(ABC):
    @abstractmethod
    def save(self, student: Student) -> None:
        pass

    @abstractmethod
    def find_by_id(self, student_id: str) -> Student | None:
        pass