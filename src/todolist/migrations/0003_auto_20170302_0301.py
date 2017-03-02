# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20170302_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='date',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='description',
        ),
        migrations.AddField(
            model_name='todolist',
            name='Add_a_to_do',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
