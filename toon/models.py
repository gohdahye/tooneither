from django.db import models

# Create your models here.


class Toon(models.Model):
    title = models.CharField(max_length=50)
    day = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField()
    head_image = models.ImageField(upload_to='toon/images/%Y/%m%d/', blank=True)
    file_upload = models.FileField(upload_to='toon/files/%Y/%m%d/', blank=True)