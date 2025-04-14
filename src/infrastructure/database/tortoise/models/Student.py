from tortoise import fields
from tortoise.models import Model


class Student(Model):
    student_id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

    class Meta:
        table = "students"