from django.db import models

# Create your models here.


class Toon(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField()
    head_image = models.ImageField(upload_to='toon/images/%Y/%m%d/', blank=True)
    file_image = models.ImageField(upload_to='toon/files/%Y/%m%d/', blank=True)

    def get_absolute_url(self):
        return f'/toon/{self.pk}/'