from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Managers.models import CustomManager
from TV_Server import Utils
from Tags.models import Tag

class Serials(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    catagory = models.ManyToManyField(Tag)

    type_choice = (
        ('S','single'),
        ('M','multi'),
    )
    type = models.CharField(max_length=1,choices=type_choice,default='S')

    title = models.CharField(max_length=20)
    describe = models.TextField(max_length=500)
    director = models.CharField(max_length=20,null=True,blank=True)
    actors = models.CharField(max_length=100,null=True,blank=True)

    release_date = models.DateTimeField(auto_now=True)

    headshot = models.ImageField(upload_to=Utils.serials_path,null=True,blank=True)

    objects = models.Manager()
    custom = CustomManager()

    class Meta:
        db_table="serials"
        get_latest_by = 'created_at'
        ordering = ['created_at']

