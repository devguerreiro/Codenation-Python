from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=50)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(protocol="IPv4", max_length=39)
    status = models.BooleanField(default=False)
