# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20151225_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_account',
            name='username',
        ),
    ]
