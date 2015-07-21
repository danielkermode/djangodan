# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danapp', '0004_auto_20150718_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='font',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
