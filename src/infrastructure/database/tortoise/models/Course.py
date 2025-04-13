from tortoise import fields
from tortoise.models import Model


class Course(Model):
    course_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    coordinator = fields.ForeignKeyField("models.AcademicCoordinator", related_name="courses")
    professors = fields.ManyToManyField("models.Professor", related_name="courses")