# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 07:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160729_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectplace',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
