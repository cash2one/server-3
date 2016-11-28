from __future__ import unicode_literals

from django.db import models

from Videos.models import Video
from Clients.models import Clients

# Create your models here.

class Top(models.Model):
    client_id = models.ForeignKey(Clients)

    class Meta:
        db_table = "top"



class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    client_id = models.ForeignKey(Clients)
    content = models.TextField()
    top = models.ForeignKey(Top)

    type_choice = (
        ('P', 'PC'),
        ('I', 'IOS'),
        ('A', 'ANDROID'),
    )

    device = models.CharField(max_length=1,choices=type_choice,default='P')
    sub_comment_id = models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = "comments"
        get_latest_by = 'created_at'
        ordering = ['created_at']

