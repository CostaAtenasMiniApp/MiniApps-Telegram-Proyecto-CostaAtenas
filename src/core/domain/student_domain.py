from datetime import datetime
from typing import Optional, List

class StudentDomain:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        registration_date: datetime,
        student_id: Optional[int] = None,
        # Sección Identificación
        national_id: Optional[str] = None,
        phone: Optional[str] = None,
        country: Optional[str] = None,
        city: Optional[str] = None,
        is_proplayas_member: bool = False,
        proplayas_node: Optional[str] = None,
        # Sección Datos Estadísticos
        belongs_to_hotel: bool = False,
        hotel_name: Optional[str] = None,
        age: Optional[int] = None,
        other_discovery_info: Optional[str] = None,
        discovery_methods: Optional[List[str]] = None,
        referral_info: Optional[str] = None,
        scholarship_code: str = "No aplica",
        education_level: Optional[str] = None,
        study_area: Optional[str] = None,
        work_area: Optional[str] = None,
        course_motivation: Optional[str] = None,
        # Sección Legal
        wants_certification_info: bool = False
    ):
        # Identificación básica
        self.student_id=student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_date = registration_date

        # Sección Identificación
        self.national_id = national_id
        self.phone = phone
        self.country = country
        self.city = city
        self.is_proplayas_member = is_proplayas_member
        self.proplayas_node = proplayas_node

        # Sección Datos Estadísticos
        self.belongs_to_hotel = belongs_to_hotel
        self.hotel_name = hotel_name
        self.age = age
        self.other_discovery_info=other_discovery_info
        self.discovery_methods = discovery_methods or []
        self.referral_info = referral_info
        self.scholarship_code = scholarship_code
        self.education_level = education_level
        self.study_area = study_area
        self.work_area = work_area
        self.course_motivation = course_motivation

        # Sección Legal
        self.wants_certification_info = wants_certification_info

    @classmethod
    def from_model(cls, student_model):
        """Método factory para crear StudentDomain desde el modelo ORM"""
        return cls(
            student_id=student_model.student_id,
            first_name=student_model.first_name,
            last_name=student_model.last_name,
            email=student_model.email,
            registration_date=student_model.registration_date,
            national_id=student_model.national_id,
            phone=student_model.phone,
            country=student_model.country,
            city=student_model.city,
            is_proplayas_member=student_model.is_proplayas_member,
            proplayas_node=student_model.proplayas_node,
            belongs_to_hotel=student_model.belongs_to_hotel,
            hotel_name=student_model.hotel_name,
            age=student_model.age,
            other_discovery_info=student_model.other_discovery_info,
            discovery_methods=student_model.discovery_method,
            referral_info=student_model.referral_info,
            scholarship_code=student_model.scholarship_code,
            education_level=student_model.education_level,
            study_area=student_model.study_area,
            work_area=student_model.work_area,
            course_motivation=student_model.course_motivation,
            wants_certification_info=student_model.wants_certification_info
        )

    def to_dict(self):
        """Convierte el dominio a diccionario para serialización"""
        return {
            # Identificación básica
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'registration_date': self.registration_date.isoformat(),

            # Sección Identificación
            'national_id': self.national_id,
            'phone': self.phone,
            'country': self.country,
            'city': self.city,
            'is_proplayas_member': self.is_proplayas_member,
            'proplayas_node': self.proplayas_node,

            # Sección Datos Estadísticos
            'belongs_to_hotel': self.belongs_to_hotel,
            'hotel_name': self.hotel_name,
            'age': self.age,
            'other_discovery_info': self.other_discovery_info,
            'discovery_methods': self.discovery_methods,
            'referral_info': self.referral_info,
            'scholarship_code': self.scholarship_code,
            'education_level': self.education_level,
            'study_area': self.study_area,
            'work_area': self.work_area,
            'course_motivation': self.course_motivation,

            # Sección Legal
            'wants_certification_info': self.wants_certification_info
        }

    def validate(self):
        """Valida los datos del dominio"""
        errors = []

        if not self.email:
            errors.append("El email es obligatorio")
        elif '@' not in self.email:
            errors.append("El email no tiene formato válido")

        if not self.first_name:
            errors.append("El nombre es obligatorio")

        if not self.last_name:
            errors.append("El apellido es obligatorio")

        if self.age is not None and (self.age < 15 or self.age > 100):
            errors.append("La edad debe estar entre 15 y 100 años")

        return errors