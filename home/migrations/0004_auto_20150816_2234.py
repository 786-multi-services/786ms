# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='type',
            new_name='service_type',
        ),
    ]
