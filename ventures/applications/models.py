from django.db import models


class Application(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.BigIntegerField()
    email_id = models.EmailField()
    idea_name = models.CharField(max_length=50)
    idea_summary = models.TextField()
