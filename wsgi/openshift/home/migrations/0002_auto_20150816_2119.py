# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'Creation time')),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Creation time'),
        ),
    ]
