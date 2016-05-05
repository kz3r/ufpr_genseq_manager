# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0007_auto_20160416_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nivel_acesso',
            field=models.ForeignKey(to='genseq.NivelAcesso', null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='status',
            field=models.ForeignKey(to='genseq.StatusUsuario', null=True),
        ),
    ]
