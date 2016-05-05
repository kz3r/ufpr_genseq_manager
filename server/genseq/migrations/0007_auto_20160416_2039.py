# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0006_auto_20160416_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='instituicao',
            field=models.ForeignKey(to='genseq.Instituicao', null=True),
        ),
    ]
