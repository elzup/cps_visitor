# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20150524_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='full_name',
            field=models.CharField(verbose_name='本名', default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='visitor',
            name='univ_id',
            field=models.CharField(verbose_name='学籍番号', default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.CharField(verbose_name='ユーザ名', max_length=64),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='nfc_id',
            field=models.CharField(verbose_name='nfcID', default=None, max_length=64),
        ),
    ]
