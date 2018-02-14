# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-13 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_video_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
