# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kemence_app', '0002_furnace_furnaceimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnaceimg',
            name='image',
            field=models.ImageField(upload_to='kemence_app/media/furnace/'),
        ),
    ]
