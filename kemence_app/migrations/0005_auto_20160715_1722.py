# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kemence_app', '0004_auto_20160715_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnace',
            name='image',
            field=models.ImageField(upload_to='kemence_app/media/furnace/%Y/%m/%d', null=True),
        ),
    ]
