from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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


class SistemaManager(models.Manager):

	def create_sistema(self, **kwargs):

		if not kwargs.get('descricao'):
			raise ValueError('Por favor, digite uma descricao.')

		sistema= self.model(
			 descricao = kwargs.get('descricao')
		)
		sistema.save()

		return sistema

class  Sistema(models.Model):
	"""Equipamentos que realizam as corridas de sequenciamento"""
	descricao = models.CharField(max_length = 50)
	objects = SistemaManager()

class ServicoManager(models.Manager):

	def create_servico(self, **kwargs):

		if not kwargs.get('descricao'):
			raise ValueError('Por favor, digite uma descricao.')

		servico = self.model(
			 descricao = kwargs.get('descricao')
		)
		servico.save()

		return servico


class  Servico(models.Model):
	"""Tipos de analises que podem ser feitas com os equipamentos"""
	descricao = models.CharField(max_length = 50)

	objects = ServicoManager()

class KitDeplecaoManager(models.Manager):

	def create_kit_deplecao(self, **kwargs):

		if not kwargs.get('descricao'):
			raise ValueError('Por favor, digite uma descricao.')

		kit_deplecao = self.model(
			 descricao = kwargs.get('descricao')
		)
		kit_deplecao.save()

		return kit_deplecao

class  KitDeplecao(models.Model):
	"""Tipos kits de deplecao utilizados na analise de cada amostra na corrida"""
	descricao = models.CharField(max_length = 50)

	objects = KitDeplecaoManager()

class UsuarioManager(BaseUserManager):

	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('Por favor, digite um email valido.')

		if not kwargs.get('nome'):
			raise ValueError('Por favor, digite o nome completo.')

		usuario = self.model(
			email = self.normalize_email(email), nome = kwargs.get('nome'), nivel_acesso = kwargs.get('nivel_acesso')
		)

		usuario.set_password(password)
		usuario.save()

		return usuario

	def create_superuser(self, email, password, **kwargs):
		usuario = self.create_user(email, password, **kwargs)

		nivel_acesso = NivelAcesso.objects.get(descricao = 'Administrador')
		usuario.nivel_acesso = nivel_acesso

		status_usuario = StatusUsuario.objects.get(descricao = 'Ativo')
		usuario.status_usuario = status_usuario

		usuario.save()

		return usuario

class Usuario(AbstractBaseUser):
	""" Usuario utilizador do sistema. Seu papel e definido pelo modelo
	NivelAcesso"""

	nivel_acesso = models.ForeignKey(NivelAcesso, null = True)
	status = models.ForeignKey(StatusUsuario, null = True)
	instituicao = models.ForeignKey(Instituicao, null = True)

	nome = models.CharField(max_length = 100, blank = False)
	telefone = models.CharField(max_length = 11, blank = True)
	setor = models.CharField(max_length = 50, blank = True)
	email = models.EmailField(max_length = 50, unique = True)

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)

	objects = UsuarioManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nome']

	def __unicode__(self):
		return self.email

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

	organismo = models.CharField(max_length = 100)
	cod_origem = models.CharField(max_length = 20, null = True, blank = True)
	qualidade = models.DecimalField(max_digits = 10, decimal_places = 3, null = True, blank = True)
	tipo = models.CharField(max_length = 1, choices = escolhas_tipo_organismo)
	observacao = models.CharField(max_length = 100, null = True, blank = True )
	autorizado_em = models.DateTimeField(null = True)

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)


class Projeto(models.Model):
	"""Projeto ao qual as amostras enviadas farao parte. Pertence a uma
	instituicao e possui usuario responsavel"""
	instituicao = models.ForeignKey(Instituicao)
	autorizado_por = models.ForeignKey(Usuario, related_name = 'projeto_usuario_autorizacao', null = True, blank = True)
	autorizado_em = models.DateTimeField(null = True, blank = True )

	nome = models.CharField(max_length = 100)
	descricao = models.TextField()
	membros = models.ManyToManyField(
		Usuario,
		through = 'UsuarioProjeto'
	)

	amostras = models.ManyToManyField(
		Amostra,
		through = 'ProjetoAmostra'
	)

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)



class UsuarioProjeto(models.Model):
	""" Relacao de projetos que um usuario participa e seu papel no mesmo """
	projeto = models.ForeignKey(Projeto, related_name='usuarioprojetos')
	usuario = models.ForeignKey(Usuario, related_name='usuarioprojetos')
	papel = models.ForeignKey(PapelProjeto)




class ProjetoAmostra(models.Model):
	"""Relacao de amostras enviadas compondo um projeto"""
	projeto = models.ForeignKey(Projeto, related_name='projetoamostras')
	amostra = models.ForeignKey(Amostra, related_name='projetoamostras')
	responsavel_envio = models.ForeignKey(Usuario)

	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)

class Corrida(models.Model):
	"""Registro da corrida de sequenciamento"""
	sistema = models.ForeignKey(Sistema)
	servico = models.ForeignKey(Servico)
	amostras = models.ManyToManyField(
		Amostra,
		through = 'AmostraCorrida'
	)

	detalhes = models.TextField()
	data_hora = models.DateTimeField(auto_now_add = True)

class AmostraCorrida(models.Model):
	amostra = models.ForeignKey(Amostra, related_name='amostrascorrida')
	corrida = models.ForeignKey(Corrida, related_name='amostrascorrida')
	kit_deplecao = models.ForeignKey(KitDeplecao)

	resultado = models.DecimalField(max_digits = 10, decimal_places = 3)
	arquivo_gerado = models.CharField(max_length = 100)
	barcode = models.CharField(max_length = 20)
	ciclos_pcr = models.IntegerField()

	criado_por = models.ForeignKey(Usuario, related_name = 'amostra_corrida_usuario_registro')
	criado_em = models.DateTimeField(auto_now_add = True)
	atualizado_em = models.DateTimeField(auto_now = True)
	atualizado_por = models.ForeignKey(Usuario, related_name = 'amostra_corrida_usuario_atualizacao')
