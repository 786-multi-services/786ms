# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-05 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_auto_20150816_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttoken',
            name='token',
            field=models.CharField(default=b'B8502D0F', editable=False, max_length=8, unique=True),
        ),
    ]
