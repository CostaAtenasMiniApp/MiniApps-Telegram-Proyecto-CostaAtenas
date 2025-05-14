from tortoise import fields
from tortoise.models import Model


class Module(Model):
    module_id = fields.IntField(pk=True)
    course_id = fields.ForeignKeyField("models.Course", related_name="modules")
    name = fields.CharField(max_length=255)
    description = fields.TextField()