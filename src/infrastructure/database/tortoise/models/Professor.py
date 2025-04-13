from tortoise import fields
from tortoise.models import Model


class Professor(Model):
    professor_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)