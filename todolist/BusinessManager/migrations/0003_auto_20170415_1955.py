# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessManager', '0002_auto_20170415_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='deadline',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='business',
            name='title',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
