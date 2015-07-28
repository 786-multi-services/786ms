# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0012_cccuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CCCUser',
        ),
    ]
