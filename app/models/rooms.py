from tortoise.models import Model
from tortoise import fields


class Room(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    basecoin = fields.IntField()
