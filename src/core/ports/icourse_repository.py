from abc import ABC, abstractmethod
from src.core.domain.course import CourseDomain

class ICourseRepository(ABC):
    @abstractmethod
    async def save(self, course: CourseDomain) -> int:
        pass

    @abstractmethod
    async def find_by_id(self, course_id: str) -> CourseDomain | None:
        pass

    @abstractmethod
    async def find_all(self) -> list[CourseDomain]:
        pass

    @abstractmethod
    async def delete(self, course_id: str) -> None:
        pass