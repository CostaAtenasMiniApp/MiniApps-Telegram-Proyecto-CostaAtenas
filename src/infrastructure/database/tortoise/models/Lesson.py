from tortoise import fields
from tortoise.models import Model


class Lesson(Model):
    lesson_id = fields.IntField(pk=True)
    module_id = fields.ForeignKeyField("models.Module", related_name="lessons")
    title = fields.CharField(max_length=255)
    content = fields.TextField()