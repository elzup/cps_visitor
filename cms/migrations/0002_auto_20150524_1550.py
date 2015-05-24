# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='ユーザ名', max_length=255)),
                ('nfc_id', models.CharField(verbose_name='nfcID', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='impression',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Impression',
        ),
        migrations.AddField(
            model_name='log',
            name='visitor',
            field=models.ForeignKey(verbose_name='ユーザ', related_name='logs', to='cms.Visitor'),
        ),
    ]
