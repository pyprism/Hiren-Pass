# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0012_recent_accessed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordfieldhistory',
            name='iteration',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vault',
            name='iteration',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
