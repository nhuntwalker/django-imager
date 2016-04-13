# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0007_auto_20160411_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to=settings.AUTH_USER_MODEL),
        ),
    ]
