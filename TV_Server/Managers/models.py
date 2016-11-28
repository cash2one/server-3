from __future__ import unicode_literals

from django.db import models

from TV_Server import Utils

from django.conf import settings



class CustomManager(models.Manager):
    def get_queryset(self):
        return super(CustomManager,self).get_queryset()


    def add_images_url(self):
        query = self.get_queryset()
        for item in query:
            if item.headshot.name:
                item.headshot.name = settings.ALLOWED_HOSTS[0]+settings.MEDIA_URL+item.headshot.name
        return query

    def get_single(self,*args, **kwargs):

        query = self.get_queryset().filter(*args, **kwargs)
        for item in query:
            if item.headshot.name:
                item.headshot.name = settings.ALLOWED_HOSTS[0] + settings.MEDIA_URL + item.headshot.name
        return query



# Create your models here.
class Manager(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    headshot = models.ImageField(upload_to=Utils.avator_path,null=True,blank=True)
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    custom = CustomManager()


    def save(self, *args, **kwargs):
        self.password = Utils.makepassword(self.password)
        super(Manager, self).save(*args,**kwargs)

    def is_authenticated(self):
        return True

    def __unicode__(self):
        return self.email

    class Meta:
        db_table="manager"
        get_latest_by = 'created_at'
        ordering = ['created_at']