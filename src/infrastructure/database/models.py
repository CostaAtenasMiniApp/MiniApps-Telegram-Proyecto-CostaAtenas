from tortoise import fields
from tortoise.models import Model


class Course(Model):
    course_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    coordinator = fields.ForeignKeyField("models.AcademicCoordinator", related_name="courses")
    professors = fields.ManyToManyField("models.Professor", related_name="courses")


class Module(Model):
    module_id = fields.IntField(pk=True)
    course_id = fields.ForeignKeyField("models.Course", related_name="modules")
    name = fields.CharField(max_length=255)
    description = fields.TextField()


class Lesson(Model):
    lesson_id = fields.IntField(pk=True)
    module_id = fields.ForeignKeyField("models.Module", related_name="lessons")
    title = fields.CharField(max_length=255)
    content = fields.TextField()


class Professor(Model):
    professor_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)


class Student(Model):
    student_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)


class Enrollment(Model):
    enrollment_id = fields.IntField(pk=True)
    student_id = fields.ForeignKeyField("models.Student", related_name="enrollments")
    course_id = fields.ForeignKeyField("models.Course", related_name="enrollments")
    enrollment_date = fields.DatetimeField(auto_now_add=True)


class Evaluation(Model):
    evaluation_id = fields.IntField(pk=True)
    course_id = fields.ForeignKeyField("models.Course", related_name="evaluations")
    module_id = fields.ForeignKeyField("models.Module", related_name="evaluations")
    score = fields.IntField()
    feedback = fields.TextField()


class AcademicCoordinator(Model):
    coordinator_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)