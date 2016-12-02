# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='cod_origem',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='amostra',
            name='qualidade',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
        ),
    ]
