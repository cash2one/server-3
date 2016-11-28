from __future__ import unicode_literals

from django.db import models

from Managers.models import Manager

from django.db import connection


# Create your models here.

class TagManager(models.Manager):
    def getTags(self):
        cursor = connection.cursor()
        cursor.execute("select tags.title, manager.nickname,tags.created_at from tags,manager where tags.manager_id=manager.id ORDER BY tags.created_at DESC")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(title=row[0], manager_id=row[1], created_at=row[2])
            result_list.append(p)
        return result_list

    def get_queryset(self):
        return self.getTags()

class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=10)
    manager = models.ForeignKey(Manager)

    objects = models.Manager()
    tags = TagManager()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table="tags"
        get_latest_by = 'created_at'
        ordering = ['created_at']
