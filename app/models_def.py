from tortoise.models import Model
from tortoise import fields


class IpAddresses(Model):
    id = fields.IntField(pk=True)
    ip = fields.CharField(max_length=255, unique=True)
    used = fields.BooleanField(default=False)
    comment = fields.CharField(max_length=255, null = True, blank = True, default=None)

    def __str__(self):
        return self.name

class Networks(Model):
    id = fields.IntField(pk=True)
    network = fields.CharField(max_length=255, unique=True)
    active = fields.BooleanField(default=False)





    def __str__(self):
        return self.name
