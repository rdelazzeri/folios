from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import User
from datetime import datetime    


class Folio(models.Model):
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=600)
    content = models.TextField(max_length=6000)
    date_post = models.DateTimeField()
    date_ini = models.DateField()
    date_end = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.title
    
class Picture(models.Model):
    title = models.CharField(max_length=80)
    desc = models.CharField(max_length=600)
    file = models.FileField(upload_to='media/pics')
    date_post = models.DateTimeField()
    folio = models.ForeignKey(Folio, on_delete=CASCADE, null=True)


class Link(models.Model):
    title = models.CharField(max_length=80)
    desc = models.CharField(max_length=600)
    link = models.URLField()
    date_post = models.DateTimeField()
    folio = models.ForeignKey(Folio, on_delete=CASCADE, null=True)
