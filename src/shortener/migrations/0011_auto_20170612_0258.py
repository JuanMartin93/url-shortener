# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-12 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0010_auto_20170611_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurl',
            name='url',
            field=models.CharField(max_length=200, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
