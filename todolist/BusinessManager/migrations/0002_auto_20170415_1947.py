# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='statues',
            new_name='status',
        ),
    ]
