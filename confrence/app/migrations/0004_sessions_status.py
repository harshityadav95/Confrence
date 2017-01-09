# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-09 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170109_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='status',
            field=models.CharField(choices=[('a', 'Approved'), ('s', 'Submitted'), ('r', 'Rejected')], default='a', max_length=1),
            preserve_default=False,
        ),
    ]