# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_account_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
