# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0009_auto_20150709_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.ForeignKey(blank=True, to='career.Token', null=True),
        ),
    ]
