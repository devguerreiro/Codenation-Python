from django.db import models

from django.core.validators import MinLengthValidator


class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
