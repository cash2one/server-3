# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.FileField(upload_to='video'),
        ),
    ]
