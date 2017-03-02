# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20170302_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='created',
            field=models.DateField(null=True, blank=True),
        ),
    ]
