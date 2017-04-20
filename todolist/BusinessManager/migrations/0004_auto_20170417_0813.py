# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessManager', '0003_auto_20170415_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='business',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
