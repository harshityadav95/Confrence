# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tracks',
            new_name='Track',
        ),
    ]
