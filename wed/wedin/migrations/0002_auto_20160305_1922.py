# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
