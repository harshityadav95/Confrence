# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('abstract', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='sessions',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Speaker'),
        ),
        migrations.AddField(
            model_name='sessions',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tracks'),
        ),
    ]
