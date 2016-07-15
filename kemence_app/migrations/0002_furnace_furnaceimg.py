# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kemence_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furnace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FurnaceImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='media/furnace/')),
                ('furnace', models.ForeignKey(to='kemence_app.Furnace', related_name='images')),
            ],
        ),
    ]
