from tortoise import fields
from tortoise.models import Model


class StudentDiscoveryMethod(Model):
    student = fields.ForeignKeyField("models.Student", related_name="discovery_links")
    method = fields.ForeignKeyField("models.DiscoveryMethod"
        , related_name="student_links"
    )
    details = fields.TextField(
        null=True,
        description="Detalles específicos (ej. nombre de quien refirió)"
    )
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "student_discovery_methods"