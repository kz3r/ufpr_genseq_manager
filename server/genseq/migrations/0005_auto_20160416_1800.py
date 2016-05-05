# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0004_auto_20160416_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='responsavel',
            field=models.ForeignKey(to='genseq.Usuario', null=True),
        ),
    ]
