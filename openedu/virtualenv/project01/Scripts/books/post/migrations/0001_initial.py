# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-01 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.CharField(max_length=300, verbose_name='Текст рассказа')),
            ],
        ),
    ]
