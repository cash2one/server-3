from __future__ import unicode_literals

from django.db import models

from Managers.models import Manager

from Serials.models import Serials
from django.conf import settings

from django.db import connection


class VideoManager(models.Manager):
    def getVideos(self):
        cursor = connection.cursor()
        cursor.execute("select title, manager_id, serials_id, video_url from video ORDER BY created_at DESC")
        result_list = []
        for row in cursor.fetchall():
            path = settings.ALLOWED_HOSTS[0]+settings.MEDIA_URL+row[3]
            p = self.model(title=row[0], manager_id=row[1], serials_id=row[2],video_url=path)
            result_list.append(p)
        return result_list

    def get_queryset(self):
        return self.getVideos()

class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    video_id = models.AutoField(primary_key=True)
    play_num = models.IntegerField(default=0)

    title = models.CharField(max_length=20,null=True,blank=True)
    describe = models.TextField(max_length=500,null=True,blank=True)
    video_url = models.FileField(upload_to='video')


    manager = models.ForeignKey(Manager)
    serials = models.ForeignKey(Serials,on_delete=models.CASCADE)

    objects = models.Manager()
    videos = VideoManager()

    class Meta:
        db_table="video"
        get_latest_by = 'created_at'
        ordering = ['created_at']