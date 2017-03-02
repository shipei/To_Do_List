# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20170302_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='Add_a_to_do',
            new_name='description',
        ),
    ]
