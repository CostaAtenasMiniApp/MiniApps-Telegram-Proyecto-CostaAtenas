from abc import ABC, abstractmethod
from src.core.domain.student_domain import StudentDomain

class IStudentRepository(ABC):
    @abstractmethod
    async def save(self, student: StudentDomain) -> int:
        pass

    @abstractmethod
    async def find_by_id(self, student_id: str) -> StudentDomain | None:
        pass

    @abstractmethod
    async def find_all(self) -> list[StudentDomain]:
        pass

    @abstractmethod
    async def delete(self, student_id: str) -> None:
        pass