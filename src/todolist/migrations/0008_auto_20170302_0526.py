# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20170302_0525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='Due_on',
            new_name='due_on',
        ),
    ]
