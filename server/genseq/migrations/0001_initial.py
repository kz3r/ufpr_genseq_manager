# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11, blank=True)),
                ('setor', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organismo', models.CharField(max_length=100)),
                ('cod_origem', models.CharField(max_length=20)),
                ('qualidade', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('tipo', models.CharField(max_length=1, choices=[(b'O', b'Organismo'), (b'G', b'Gel')])),
                ('observacao', models.CharField(max_length=100, null=True, blank=True)),
                ('autorizado_em', models.DateTimeField(null=True)),
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
                ('amostra', models.ForeignKey(related_name='amostrascorrida', to='genseq.Amostra')),
                ('atualizado_por', models.ForeignKey(related_name='amostra_corrida_usuario_atualizacao', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Corrida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalhes', models.TextField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('amostras', models.ManyToManyField(to='genseq.Amostra', through='genseq.AmostraCorrida')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
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
            name='NivelAcesso',
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
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autorizado_em', models.DateTimeField(null=True, blank=True)),
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
                ('amostra', models.ForeignKey(related_name='projetoamostras', to='genseq.Amostra')),
                ('projeto', models.ForeignKey(related_name='projetoamostras', to='genseq.Projeto')),
                ('responsavel_envio', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
        migrations.CreateModel(
            name='StatusUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('papel', models.ForeignKey(to='genseq.PapelProjeto')),
                ('projeto', models.ForeignKey(related_name='usuarioprojetos', to='genseq.Projeto')),
                ('usuario', models.ForeignKey(related_name='usuarioprojetos', to=settings.AUTH_USER_MODEL)),
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
            field=models.ForeignKey(related_name='projeto_usuario_autorizacao', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='instituicao',
            field=models.ForeignKey(to='genseq.Instituicao'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='genseq.UsuarioProjeto'),
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
            field=models.ForeignKey(related_name='amostrascorrida', to='genseq.Corrida'),
        ),
        migrations.AddField(
            model_name='amostracorrida',
            name='criado_por',
            field=models.ForeignKey(related_name='amostra_corrida_usuario_registro', to=settings.AUTH_USER_MODEL),
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
        migrations.AddField(
            model_name='usuario',
            name='instituicao',
            field=models.ForeignKey(to='genseq.Instituicao', null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nivel_acesso',
            field=models.ForeignKey(to='genseq.NivelAcesso', null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='status',
            field=models.ForeignKey(to='genseq.StatusUsuario', null=True),
        ),
    ]
