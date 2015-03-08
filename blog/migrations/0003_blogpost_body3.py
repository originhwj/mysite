# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150114_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='body3',
            field=models.TextField(default=datetime.datetime(2015, 1, 14, 8, 16, 54, 300000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
