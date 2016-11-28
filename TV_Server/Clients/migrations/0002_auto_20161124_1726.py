# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0002_auto_20161124_1647'),
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='clients',
            name='videohistory',
        ),
        migrations.AddField(
            model_name='history',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Clients'),
        ),
        migrations.AddField(
            model_name='history',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Videos.Video'),
        ),
        migrations.AddField(
            model_name='collections',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Clients'),
        ),
        migrations.AddField(
            model_name='collections',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Videos.Video'),
        ),
    ]