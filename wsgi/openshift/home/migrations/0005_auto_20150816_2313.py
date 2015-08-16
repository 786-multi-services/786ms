# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150816_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'Creation time')),
                ('object_type', models.IntegerField(choices=[(1, b'News'), (2, b'Programme')])),
            ],
        ),
        migrations.DeleteModel(
            name='NewsObject',
        ),
    ]
