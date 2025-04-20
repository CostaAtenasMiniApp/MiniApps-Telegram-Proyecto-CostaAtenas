from tortoise import fields
from tortoise.models import Model


class DiscoveryMethod(Model):
    method_id = fields.IntField(pk=True)
    name = fields.CharField(
        max_length=100,
        unique=True,
        description="Método por el cual el estudiante conoció el curso"
    )
    category = fields.CharField(
        max_length=50,
        description="Categoría del método (social_media, referral, etc.)"
    )
    icon = fields.CharField(
        max_length=50,
        null=True,
        description="Icono de FontAwesome o similar para representación visual"
    )
    is_active = fields.BooleanField(default=True)

    class Meta:
        ordering = ["category", "name"]
        table = "discovery_methods"

