# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('statues', models.SmallIntegerField(default=1)),
                ('deadline', models.DateTimeField()),
                ('owner', models.CharField(max_length=20)),
            ],
        ),
    ]
