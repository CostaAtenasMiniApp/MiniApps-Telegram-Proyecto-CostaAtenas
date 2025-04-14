from tortoise import fields
from tortoise.models import Model
from datetime import date


class Course(Model):
    course_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    start_date = fields.DateField()
    duration = fields.IntField()  # Assuming duration is in days or weeks
    status = fields.CharField(max_length=50)  # Adjust max_length as needed
    coordinator = fields.ForeignKeyField("models.AcademicCoordinator", related_name="courses")
    professors = fields.ManyToManyField("models.Professor", related_name="courses")