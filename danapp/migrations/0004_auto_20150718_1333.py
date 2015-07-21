# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danapp', '0003_auto_20150718_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='colour',
            field=models.CharField(max_length=10, choices=[(b'Blue', b'Blue'), (b'Red', b'Red'), (b'Yellow', b'Yellow')]),
            preserve_default=True,
        ),
    ]
