# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kemence_app', '0003_auto_20160715_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furnaceimg',
            name='furnace',
        ),
        migrations.AddField(
            model_name='furnace',
            name='image',
            field=models.ImageField(null=True, upload_to='kemence_app/media/furnace/'),
        ),
        migrations.DeleteModel(
            name='FurnaceImg',
        ),
    ]
