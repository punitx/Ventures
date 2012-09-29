from django.db import models
from ventures.volunteers import ROLE_OPTIONS


class Volunteer(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.BigIntegerField()
    email_id = models.EmailField()
    role = models.CharField(max_length=3, choices=ROLE_OPTIONS)
