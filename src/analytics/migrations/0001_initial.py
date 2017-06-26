# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-17 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0011_auto_20170612_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('kirr_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.KUrl')),
            ],
        ),
    ]
