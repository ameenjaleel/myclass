# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170315_0846'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='User',
        ),
    ]
