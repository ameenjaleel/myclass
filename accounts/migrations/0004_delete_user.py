# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170315_0905'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
