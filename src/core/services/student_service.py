# core/services/user_service.py
from src.core.ports.istudent_repository import IStudentRepository
from src.core.domain.student_domain import StudentDomain

class StudentService:
    def __init__(self, student_repository: IStudentRepository):
        self.student_repository = student_repository

    async def create_student(self, student:StudentDomain) -> StudentDomain:
        await self.student_repository.save(student)
        return student

    async def get_student_by_id(self, student_id: int) -> StudentDomain:
        return await self.student_repository.find_by_id(student_id)

    async def get_all_students(self) -> list[StudentDomain]:
        return await self.student_repository.find_all()

    async def update_student(self, student_id: int,
                            first_name: str = None,
                            last_name: str = None,
                            email: str = None,
                            phone: str = None,
                            country: str = None,
                            city: str = None,
                            age: int = None,
                            national_id: str = None,
                            is_proplayas_member: bool = None,
                            proplayas_node: str = None,
                            belongs_to_hotel: bool = None,
                            hotel_name: str = None,
                            other_discovery_info: str = None,
                            #discovery_methods: List[str] = None,
                            referral_info: str = None,
                            scholarship_code: str = None,
                            education_level: str = None,
                            study_area: str = None,
                            work_area: str = None,
                            course_motivation: str = None,
                            wants_certification_info: bool = None) -> StudentDomain:
        student = await self.student_repository.find_by_id(student_id)
        if not student:
            raise ValueError("Student not found")

        # Actualización de campos básicos
        if first_name is not None:
            student.first_name = first_name
        if last_name is not None:
            student.last_name = last_name
        if email is not None:
            student.email = email
        if phone is not None:
            student.phone = phone
        if country is not None:
            student.country = country
        if city is not None:
            student.city = city
        if age is not None:
            student.age = age

        # Actualización de campos adicionales
        if national_id is not None:
            student.national_id = national_id
        if is_proplayas_member is not None:
            student.is_proplayas_member = is_proplayas_member
        if proplayas_node is not None:
            student.proplayas_node = proplayas_node
        if belongs_to_hotel is not None:
            student.belongs_to_hotel = belongs_to_hotel
        if hotel_name is not None:
            student.hotel_name = hotel_name
        if other_discovery_info is not None:
            student.other_discovery_info = other_discovery_info
        """ if discovery_methods is not None:
            student.discovery_methods = discovery_methods """
        if referral_info is not None:
            student.referral_info = referral_info
        if scholarship_code is not None:
            student.scholarship_code = scholarship_code
        if education_level is not None:
            student.education_level = education_level
        if study_area is not None:
            student.study_area = study_area
        if work_area is not None:
            student.work_area = work_area
        if course_motivation is not None:
            student.course_motivation = course_motivation
        if wants_certification_info is not None:
            student.wants_certification_info = wants_certification_info

        await self.student_repository.save(student)
        return student

    async def delete_student(self, student_id: int) -> None:
        student = await self.student_repository.find_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        await self.student_repository.delete(student_id)