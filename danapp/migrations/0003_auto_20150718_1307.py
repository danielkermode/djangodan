# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danapp', '0002_auto_20150718_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='picture',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
