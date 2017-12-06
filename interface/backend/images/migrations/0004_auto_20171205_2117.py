# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_imagefile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagefile',
            options={'ordering': ['slice_location']},
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='path',
            field=models.FilePathField(max_length=512, path='/images', recursive=True),
        ),
    ]
