from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Days(models.Model):
    day = models.CharField(max_length=10)
    full = models.CharField(max_length=40, null=True, blank=True,)
    korean = models.CharField(max_length=40, null=True, blank=True,)
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True)

    def __str__(self):
        return self.day

    def get_absolute_url(self):
        return f'/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Days'


class Toon(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField()
    head_image = models.ImageField(upload_to='toon/images/%Y/%m%d/', blank=True)
    file_image = models.ImageField(upload_to='toon/files/%Y/%m%d/', blank=True)
    day = models.ForeignKey(Days, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/{self.day.slug}/{self.pk}/'

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

