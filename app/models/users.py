from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    password = fields.TextField()
    coins = fields.IntField()

    class Meta:
        table = "user"
