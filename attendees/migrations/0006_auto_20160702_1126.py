# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-02 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0005_auto_20150729_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]