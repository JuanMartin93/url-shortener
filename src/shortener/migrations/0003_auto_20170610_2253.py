# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-10 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_kurl_shortener'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurl',
            name='shortener',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
