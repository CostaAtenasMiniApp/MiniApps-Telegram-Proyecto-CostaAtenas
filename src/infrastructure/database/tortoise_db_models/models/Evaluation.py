from tortoise import fields
from tortoise.models import Model


class Evaluation(Model):
    evaluation_id = fields.IntField(pk=True)
    course_id = fields.ForeignKeyField("models.Course", related_name="evaluations")
    module_id = fields.ForeignKeyField("models.Module", related_name="evaluations")
    score = fields.IntField()
    feedback = fields.TextField()