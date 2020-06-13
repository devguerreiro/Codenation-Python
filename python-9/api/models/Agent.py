from django.db import models

from django.core.validators import ip_address_validators


class Agent(models.Model):
    name = models.CharField(max_length=50)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.CharField(max_length=39, validators=[ip_address_validators])
    status = models.BooleanField(default=False)
