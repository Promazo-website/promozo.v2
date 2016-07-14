# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160428_0648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessuser',
            name='settings',
        ),
        migrations.RemoveField(
            model_name='student',
            name='settings',
        ),
        migrations.AlterField(
            model_name='university',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
