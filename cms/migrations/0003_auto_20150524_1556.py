# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150524_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='timestamp',
            new_name='created_at',
        ),
    ]
