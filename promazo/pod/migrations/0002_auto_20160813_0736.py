# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pod', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podmembers',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pod.podRole'),
        ),
    ]
