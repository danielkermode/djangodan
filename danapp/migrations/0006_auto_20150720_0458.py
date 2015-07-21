# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danapp', '0005_auto_20150718_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='colour',
            field=models.CharField(default=b'Blue', max_length=10, choices=[(b'blue', b'blue'), (b'red', b'red'), (b'yellow', b'yellow')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences',
            name='font',
            field=models.CharField(default=b'Times New Roman', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
