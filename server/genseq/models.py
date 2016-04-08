from django.db import models
from django.utils	 import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Instituicao(models.Model):
	""" Cadastro da instituicao de ensino/pesquisa """
	nome = models.CharField(max_length = 100)

class NivelAcesso(models.Model):
	""" Restricoes de seguranca e tipos de usuario """
	descricao = models.CharField(max_length = 50)

class StatusUsuario(models.Model):
	""" Definicao dos possiveis status de cadastro do usuario"""
	descricao = models.CharField(max_length = 50)

class  StatusAmostra(models.Model):
	"""Definicao dos possiveis status do ciclo de vida da amostra"""
	descricao = models.CharField(max_length = 50)

class  Sistema(models.Model):
	"""Equipamentos que realizam as corridas de sequenciamento"""
	descricao = models.CharField(max_length = 50)

class  Servico(models.Model):
	"""Tipos de analises que podem ser feitas com os equipamentos"""
	descricao = models.CharField(max_length = 50)

class  KitDeplecao(models.Model):
	"""Tipos kits de deplecao utilizados na analise de cada amostra na corrida"""
	descricao = models.CharField(max_length = 50)

class Usuario(models.Model):
	""" Usuario utilizador do sistema. Seu papel e definido pelo modelo
	NivelAcesso"""

	nivel_acesso = models.ForeignKey(NivelAcesso)
	responsavel = models.ForeignKey('self')
	status = models.ForeignKey(StatusUsuario)
	instituicao = models.ForeignKey(Instituicao)

	nome = models.CharField(max_length = 100, blank = False)
	telefone = models.CharField(max_length = 11, blank = True)
	setor = models.CharField(max_length = 50, blank = True)
	email = models.EmailField(max_length = 50, unique = True)

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)

	def get_full_name(self):
		return self.nome

class PapelProjeto(models.Model):
	"""Definicao do papel do usuario dentro de um projeto"""
	descricao = models.CharField(max_length = 50)

class Amostra(models.Model):
	"""Amostra do organismo que sera analisada pelas corridas de sequenciamento"""
	escolhas_tipo_organismo = (
		('O','Organismo'),
		('G','Gel')
	)

	status = models.ForeignKey(StatusAmostra)
	sistema = models.ForeignKey(Sistema)
	servico = models.ForeignKey(Servico)

	cod_origem = models.CharField(max_length = 20)
	qualidade = models.DecimalField(max_digits = 10, decimal_places = 3)
	tipo = models.CharField(max_length = 1, choices = escolhas_tipo_organismo)
	observacao = models.CharField(max_length = 100)
	autorizado_em = models.DateTimeField()

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)

class Projeto(models.Model):
	"""Projeto ao qual as amostras enviadas farao parte. Pertence a uma
	instituicao e possui usuario responsavel"""
	instituicao = models.ForeignKey(Instituicao)
	autorizado_por = models.ForeignKey(Usuario, related_name = 'projeto_usuario_autorizacao')
	autorizado_em = models.DateTimeField()

	nome = models.CharField(max_length = 100)
	descricao = models.TextField()
	membros = models.ManyToManyField(
		Usuario,
		through = 'UsuarioProjeto',
		through_fields = ('projeto','usuario')
	)

	amostras = models.ManyToManyField(
		Amostra,
		through = 'ProjetoAmostra',
		through_fields = ('projeto','amostra')
	)

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)

class UsuarioProjeto(models.Model):
	""" Relacao de projetos que um usuario participa e seu papel no mesmo """
	usuario = models.ForeignKey(Usuario)
	projeto = models.ForeignKey(Projeto)
	papel = models.ForeignKey(PapelProjeto)

class ProjetoAmostra(models.Model):
	"""Relacao de amostras enviadas compondo um projeto"""
	projeto = models.ForeignKey(Projeto)
	amostra = models.ForeignKey(Amostra)
	responsavel_envio = models.ForeignKey(Usuario)

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)

class Corrida(models.Model):
	"""Registro da corrida de sequenciamento"""
	sistema = models.ForeignKey(Sistema)
	servico = models.ForeignKey(Servico)

	detalhes = models.TextField()
	data_hora = models.DateTimeField()

class AmostraCorrida(models.Model):
	amostra = models.ForeignKey(Amostra)
	corrida = models.ForeignKey(Corrida)
	kit_deplecao = models.ForeignKey(KitDeplecao)

	resultado = models.DecimalField(max_digits = 10, decimal_places = 3)
	arquivo_gerado = models.CharField(max_length = 100)
	barcode = models.CharField(max_length = 20)
	ciclos_pcr = models.IntegerField()

	criado_por = models.ForeignKey(Usuario, related_name = 'amostra_corrida_usuario_registro')
	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)
	atualizado_por = models.ForeignKey(Usuario, related_name = 'amostra_corrida_usuario_atualizacao')









