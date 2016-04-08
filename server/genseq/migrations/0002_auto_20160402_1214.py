# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_origem', models.CharField(max_length=20)),
                ('qualidade', models.DecimalField(max_digits=10, decimal_places=3)),
                ('tipo', models.CharField(max_length=1, choices=[(b'O', b'Organismo'), (b'G', b'Gel')])),
                ('observacao', models.CharField(max_length=100)),
                ('autorizado_em', models.DateTimeField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AmostraCorrida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resultado', models.DecimalField(max_digits=10, decimal_places=3)),
                ('arquivo_gerado', models.CharField(max_length=100)),
                ('barcode', models.CharField(max_length=20)),
                ('ciclos_pcr', models.IntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('amostra', models.ForeignKey(to='genseq.Amostra')),
                ('atualizado_por', models.ForeignKey(related_name='amostra_corrida_usuario_atualizacao', to='genseq.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Corrida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalhes', models.TextField()),
                ('data_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='KitDeplecao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PapelProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatusAmostra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='corrida',
            name='servico',
            field=models.ForeignKey(to='genseq.Servico'),
        ),
        migrations.AddField(
            model_name='corrida',
            name='sistema',
            field=models.ForeignKey(to='genseq.Sistema'),
        ),
        migrations.AddField(
            model_name='amostracorrida',
            name='corrida',
            field=models.ForeignKey(to='genseq.Corrida'),
        ),
        migrations.AddField(
            model_name='amostracorrida',
            name='criado_por',
            field=models.ForeignKey(related_name='amostra_corrida_usuario_registro', to='genseq.Usuario'),
        ),
        migrations.AddField(
            model_name='amostracorrida',
            name='kit_deplecao',
            field=models.ForeignKey(to='genseq.KitDeplecao'),
        ),
        migrations.AddField(
            model_name='amostra',
            name='servico',
            field=models.ForeignKey(to='genseq.Servico'),
        ),
        migrations.AddField(
            model_name='amostra',
            name='sistema',
            field=models.ForeignKey(to='genseq.Sistema'),
        ),
        migrations.AddField(
            model_name='amostra',
            name='status',
            field=models.ForeignKey(to='genseq.StatusAmostra'),
        ),
    ]
