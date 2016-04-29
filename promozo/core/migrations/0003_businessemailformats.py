# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 02:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20160413_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessEmailFormats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('format', models.CharField(max_length=250)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Business')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
