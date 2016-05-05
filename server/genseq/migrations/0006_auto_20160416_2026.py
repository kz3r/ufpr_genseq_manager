# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0005_auto_20160416_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='admin', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
