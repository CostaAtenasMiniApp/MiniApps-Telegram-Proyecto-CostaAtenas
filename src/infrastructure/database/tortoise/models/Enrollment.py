from tortoise import fields
from tortoise.models import Model


class Enrollment(Model):
    enrollment_id = fields.IntField(pk=True)
    student_id = fields.ForeignKeyField("models.Student", related_name="enrollments")
    course_id = fields.ForeignKeyField("models.Course", related_name="enrollments")
    enrollment_date = fields.DatetimeField(auto_now_add=True)