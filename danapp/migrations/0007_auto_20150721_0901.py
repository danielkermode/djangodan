# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danapp', '0006_auto_20150720_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='picture',
            field=models.ImageField(upload_to=b'media', blank=True),
            preserve_default=True,
        ),
    ]
