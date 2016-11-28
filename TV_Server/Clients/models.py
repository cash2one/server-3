from __future__ import unicode_literals

from TV_Server import Utils

from django.db import models

from Videos.models import Video



# Create your models here.

class Clients(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=11,unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    headshot = models.ImageField(upload_to=Utils.avator_path, null=True, blank=True)

    # videocollection = models.ManyToManyField(Video)
    # videohistory = models.ManyToManyField(Video)


    class Meta:
        db_table = "clients"
        get_latest_by = 'created_at'
        ordering = ['created_at']


class Collections(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Clients,on_delete=models.CASCADE)
    video = models.ForeignKey(Video)

class History(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    video = models.ForeignKey(Video)
