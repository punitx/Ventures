from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    template = models.FileField(upload_to='resources/')
