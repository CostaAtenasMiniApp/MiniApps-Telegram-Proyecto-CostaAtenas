from tortoise import fields
from tortoise.models import Model

class Scholarship(Model):
    code = fields.CharField(max_length=50, unique=True, pk=True)  # Código CIFPLAYAS
    discount_percentage = fields.IntField()
    valid_until = fields.DateField(null=True)
    max_uses = fields.IntField(null=True)
    current_uses = fields.IntField(default=0)
    created_by = fields.ForeignKeyField(
        "models.Professor", 
        null=True,
        related_name="created_scholarships",
        description="Profesor que creó la beca"
    )
    applicable_courses = fields.ManyToManyField(
        "models.Course",
        related_name="available_scholarships",
        description="Cursos aplicables para esta beca"
    )