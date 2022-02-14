from django.db import models

# Create your models here.


class Toon(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField()