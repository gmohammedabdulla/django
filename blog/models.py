from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)



    def __str__(self):
        return self.title

class Latlag(models.Model):
    lat = models.CharField(max_length=200)
    lag = models.CharField(max_length=200)
    area = models.TextField()
