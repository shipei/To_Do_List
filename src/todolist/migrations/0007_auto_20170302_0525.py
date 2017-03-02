# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_todolist_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='created',
            new_name='Due_on',
        ),
    ]
