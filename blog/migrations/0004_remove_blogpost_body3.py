# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_body3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='body3',
        ),
    ]
