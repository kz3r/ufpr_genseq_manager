# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genseq', '0002_auto_20160402_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autorizado_em', models.DateTimeField()),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetoAmostra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('amostra', models.ForeignKey(to='genseq.Amostra')),
                ('projeto', models.ForeignKey(to='genseq.Projeto')),
                ('responsavel_envio', models.ForeignKey(to='genseq.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('papel', models.ForeignKey(to='genseq.PapelProjeto')),
                ('projeto', models.ForeignKey(to='genseq.Projeto')),
                ('usuario', models.ForeignKey(to='genseq.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='projeto',
            name='amostras',
            field=models.ManyToManyField(to='genseq.Amostra', through='genseq.ProjetoAmostra'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='autorizado_por',
            field=models.ForeignKey(related_name='projeto_usuario_autorizacao', to='genseq.Usuario'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='instituicao',
            field=models.ForeignKey(to='genseq.Instituicao'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(to='genseq.Usuario', through='genseq.UsuarioProjeto'),
        ),
    ]
