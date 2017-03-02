# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20170302_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='description',
            new_name='task',
        ),
    ]
