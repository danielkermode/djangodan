# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danapp', '0007_auto_20150721_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='picture',
            field=models.ImageField(default=b'/media/media/defaultim.jpg', upload_to=b'media', blank=True),
            preserve_default=True,
        ),
    ]
