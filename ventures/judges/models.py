from django.db import models


class Judge(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='judges/photo')
