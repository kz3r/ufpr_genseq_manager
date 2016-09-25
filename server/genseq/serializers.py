from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from genseq.models import StatusUsuario, Usuario, Servico, Sistema, KitDeplecao, Instituicao, Projeto, UsuarioProjeto, PapelProjeto, NivelAcesso, Amostra, ProjetoAmostra

class NivelAcessoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = NivelAcesso

		fields = ('id','descricao')

class UsuarioSerializer(serializers.ModelSerializer):
	password = serializers.CharField (write_only = True, required = False)
	confirm_password = serializers.CharField (write_only = True, required = False)
	class Meta:
		model = Usuario

		fields = ('id','nivel_acesso', 'status', 'instituicao',
					 'nome', 'telefone', 'setor', 'email',
					 'password', 'confirm_password',)

		read_only_fields = ('criado_em', 'atualizado_em',)

		def create(self, validated_data):
			return Usuario.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.nome = validated_data.get('nome', instance.nome)
			instance.nivel_acesso = validated_data.get('nivel_acesso', instance.nivel_acesso)
			instance.status = validated_data.get('status', instance.status)
			instance.instituicao = validated_data.get('instituicao', instance.instituicao)
			instance.telefone = validated_data.get('telefone', instance.telefone)
			instance.setor = validated_data.get('setor', instance.setor)
			instance.email = validated_data.get('email', instance.email)

			instance.save()

			password = validated_data.get('password', None)
			confirm_password = validated_data.get('confirm_password', None)

			if password and confirm_password and password == confirm_password:
				instance.set_password(password)
				instance.save()

			update_session_auth_hash(self.context.get('request'), instance)

			return instance



class SistemaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sistema
		fields = ('id', 'descricao')

		def create(self, validated_data):
			return Sistema.objects.create(**validated_data)
		def update(self, instance, validated_data):
			instance.descricao  = validated_data.get('descricao', instance.descricao)

			instance.save()

			return instance

class ServicoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servico
		fields = ('id', 'descricao')

		def create(self, validated_data):
			return Servico.objects.create(**validated_data)
		def update(self, instance, validated_data):
			instance.descricao  = validated_data.get('descricao', instance.descricao)

			instance.save()

			return instance


class PapelProjetoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = PapelProjeto

		fields = ('id','descricao')

class InstituicaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instituicao
		fields = ('id', 'nome')

		def create(self, validated_data):
			return Instituicao.objects.create(**validated_data)
		def update(self, instance, validated_data):
			instance.nome  = validated_data.get('nome', instance.nome)

			instance.save()

			return instance

class AmostraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Amostra
		fields = ('id', 'sistema', 'servico', 'tipo', 'status','organismo')

class AmostraReadSerializer(AmostraSerializer):
	sistema = SistemaSerializer()
	servico = ServicoSerializer()

	class Meta:
		model = Amostra
		fields = ('id', 'sistema', 'servico', 'tipo', 'status','organismo')

class UsuarioProjetoSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsuarioProjeto
		fields = ('id', 'usuario','papel','projeto')

	def create(self, validated_data):
		return UsuarioProjeto.objects.create(**validated_data)


class UsuarioProjetoReadSerializer(UsuarioProjetoSerializer):
	usuario = UsuarioSerializer()
	papel = PapelProjetoSerializer()
	class Meta:
		model = UsuarioProjeto
		fields = ('id','usuario','papel')

class ProjetoAmostraSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjetoAmostra
		fields = ('id', 'projeto', 'amostra', 'responsavel_envio')

class ProjetoAmostraReadSerializer(ProjetoAmostraSerializer):
	amostra = AmostraReadSerializer()

	class Meta:
		model = ProjetoAmostra
		fields = ('id', 'amostra')

class ProjetoSerializer(serializers.ModelSerializer):

	
	class Meta:
		model = Projeto

		fields = ('id', 'nome', 'descricao', 'instituicao', 'criado_em', 'atualizado_em', 'autorizado_em')

	def create(self, validated_data):
		return Projeto.objects.create(**validated_data)

class ProjetoReadSerializer(ProjetoSerializer):
    instituicao = InstituicaoSerializer()
    membros = UsuarioProjetoReadSerializer(many=True, source='usuarioprojetos')
    amostras = ProjetoAmostraReadSerializer(many=True, source='projetoamostras')
    class Meta:

		model = Projeto

		fields = ('id', 'nome', 'descricao', 'instituicao', 'criado_em', 'atualizado_em', 'autorizado_em','membros', 'amostras')

class KitDeplecaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = KitDeplecao
		fields = ('id', 'descricao')

		def create(self, validated_data):
			return KitDeplecao.objects.create(**validated_data)
		def update(self, instance, validated_data):
			instance.descricao  = validated_data.get('descricao', instance.descricao)

			instance.save()

			return instance

class StatusUsuarioSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = StatusUsuario

		fields = ('id','descricao')

		def create(self, validated_data):
			return StatusUsuario.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.descricao = validated_data.get('descricao', instance.descricao)

			instance.save()

			return instance



