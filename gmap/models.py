from django.db import models
from django.utils import timezone

class Post(models.Model):
  map_lat = models.CharField(u'Latitude', maxlength=25, blank=True, null=True)
  map_lon = models.CharField(u'Longitude', maxlength=25, blank=True, null=True)






