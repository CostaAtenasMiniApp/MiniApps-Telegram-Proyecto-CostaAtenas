# core/services/user_service.py
from src.core.ports.icourse_repository import ICourseRepository
from src.core.domain.course import CourseDomain
from datetime import date

class CourseService:
    def __init__(self, course_repository: ICourseRepository):
        self.course_repository = course_repository

    async def create_course(self, course:CourseDomain) -> CourseDomain:
        await self.course_repository.save(course)
        return course

    async def get_course_by_id(self, id_course: int) -> CourseDomain:
        return await self.course_repository.find_by_id(id_course)

    async def get_all_course(self) -> list[CourseDomain]:
        return await self.course_repository.find_all()

    async def update_course(self, id_course: int
                            , name: str = None
                            , description: str = None
                            , start_date: date = None
                            , duration: int = None
                            , status: str = None) -> CourseDomain:
            course = await self.course_repository.find_by_id(id_course)
            if not course:
                raise ValueError("Course not found")
            if name:
                course.name = name
            if description:
                course.description = description
            if duration:
                course.duration = duration
            if status:
                course.status = status
            await self.course_repository.save(course)
            return course

    async def delete_course(self, id_course: int) -> None:
        course = await self.course_repository.find_by_id(id_course)
        if not course:
            raise ValueError("Course not found")
        await self.course_repository.delete(id_course)