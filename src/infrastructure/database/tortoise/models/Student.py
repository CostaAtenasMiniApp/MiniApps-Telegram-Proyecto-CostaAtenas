from tortoise import fields
from tortoise.models import Model


class Student(Model):
    student_id = fields.IntField(pk=True)

    # SECCIÓN IDENTIFICACIÓN
    email = fields.CharField(max_length=255
        , unique=True
        , description="Correo electrónico"
    )
    first_name = fields.CharField(max_length=255, description="Nombres")
    last_name = fields.CharField(max_length=255, description="Apellidos")
    national_id = fields.CharField(
        max_length=50,
        unique=True,
        null=True,
        description="Número documento nacional de identidad"
    )
    phone = fields.CharField(
        max_length=20,
        null=True,
        description="Número de teléfono (vinculado a Telegram)"
    )
    country = fields.CharField(max_length=100, null=True, description="País")

    city = fields.CharField(max_length=100, null=True, description="Ciudad")

    is_proplayas_member = fields.BooleanField(
        default=False,
        description="Miembro de la Red Proplayas?"
    )
    proplayas_node = fields.CharField(
        max_length=255,
        null=True,
        description="Nodo Proplayas (solo si es miembro Proplayas)"
    )

    # SECCIÓN DATOS ESTADÍSTICOS
    belongs_to_hotel = fields.BooleanField(
        default=False,
        description="Pertenece a algún hotel?"
    )
    hotel_name = fields.CharField(
        max_length=255,
        null=True,
        description="Nombre del hotel"
    )
    age = fields.IntField(null=True, description="Edad")

    discovery_methods = fields.ManyToManyField(
        "models.DiscoveryMethod",
        through="student_discovery_methods",
        related_name="students"
    )
    other_discovery_info = fields.TextField(
        null=True,
        description="Detalles adicionales cuando se selecciona 'Otro'"
    )
    referral_info = fields.TextField(
        null=True,
        description="Referido por un amigo/colega o información adicional"
    )

    scholarship = fields.ForeignKeyField(
        "models.Scholarship",
        null=True,
        related_name="awarded_students"
    )
    education_level = fields.CharField(
        max_length=100,
        null=True,
        description="Nivel educacional"
    )
    study_area = fields.CharField(
        max_length=255,
        null=True,
        description="Área de estudios"
    )
    work_area = fields.CharField(
        max_length=255,
        null=True,
        description="Área laboral o de interés"
    )
    course_motivation = fields.TextField(
        null=True,
        description="Por qué quieres realizar el curso móvil?"
    )

    # SECCIÓN LEGAL
    wants_certification_info = fields.BooleanField(
        default=False,
        description="¿Recibir información sobre certificación y gestión de playas?"
    )

    # Campos existentes
    registration_date = fields.DatetimeField(auto_now_add=True)
    enrolled_courses = fields.ManyToManyField("models.Course", related_name="students")

    class Meta:
        table = "students"
        description = "Información completa de estudiantes incluyendo datos de identificación, estadísticos y legales"