# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blogpost_body3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'photos')),
                ('caption', models.CharField(max_length=250, blank=True)),
                ('item', models.ForeignKey(to='blog.Item')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=None,
            managers=None,
        ),
    ]
