# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='書籍名')),
                ('publisher', models.CharField(max_length=255, verbose_name='出版社', blank=True)),
                ('page', models.IntegerField(default=0, verbose_name='ページ数', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='コメント', blank=True)),
                ('book', models.ForeignKey(related_name='impressions', to='cms.Book', verbose_name='書籍')),
            ],
        ),
    ]
