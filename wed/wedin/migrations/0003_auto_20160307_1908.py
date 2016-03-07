# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('wedin', '0002_auto_20160305_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
