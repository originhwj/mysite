# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='body2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
