# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0003_auto_20160402_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='responsavel',
            field=models.ForeignKey(to='genseq.Usuario', blank=True),
        ),
    ]
