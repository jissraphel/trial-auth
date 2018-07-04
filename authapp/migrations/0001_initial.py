# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-03 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=40)),
                ('artist', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('duration', models.IntegerField(max_length=40)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.Album')),
            ],
        ),
    ]
