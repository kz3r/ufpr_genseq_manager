# coding=UTF-8

import json

from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views, permissions, viewsets
from rest_framework.response import Response
from rest_framework import generics

from genseq.permissions import IsAccountOwner
from genseq.models import Usuario, Servico, Sistema, KitDeplecao, Instituicao, Projeto, UsuarioProjeto, PapelProjeto, Amostra, ProjetoAmostra, Corrida, AmostraCorrida
from genseq.serializers import UsuarioSerializer, ServicoSerializer, SistemaSerializer, KitDeplecaoSerializer, InstituicaoSerializer, ProjetoSerializer,ProjetoReadSerializer, UsuarioProjetoSerializer, PapelProjetoSerializer, AmostraSerializer, AmostraReadSerializer, ProjetoAmostraSerializer, CorridaSerializer, CorridaReadSerializer, AmostraCorridaSerializer, AmostraCorridaReadSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			Usuario.objects.create_user(**serializer.validated_data)

			response = Response(serializer.validated_data, status = status.HTTP_201_CREATED)
			response['Access-Control-Allow-Origin'] = '*'
			response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

			return response

		return Response({
			'status': 'Bad request',
			'message': 'Usuario nao pode ser inserido com os dados recebidos'
		}, status = status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
	def post(self, request, format=None):
		print('IM IN')

		data = json.loads(request.body.decode())


		email = data.get('email', None)
		password = data.get('password', None)

		usuario = authenticate(email = email, password = password)

		if usuario is not None:
			if usuario.is_active:
				login(request, usuario)

				serialized = UsuarioSerializer(usuario)

				return Response(serialized.data)
			else:
				return Response({
					'status': 'Unauthorized',
					'message': 'Sua conta está desativada'
				}, status = status.HTTP_401_UNAUTHORIZED)
		else:
			return Response({
				'status': 'Unauthorized',
				'message': 'Nome de usuário ou senha inválidos'
			}, status = status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
	
	#PERMISSION CLASS BLOQUEANDO O ACESSO. PORQUE?
	#permission_classes = (permissions.IsAuthenticated,)
	#print(permission_classes)

	def post(self, request, format=None):
		logout(request)

		return Response({}, status = status.HTTP_204_NO_CONTENT)

class ServicoViewSet(viewsets.ModelViewSet):
	queryset = Servico.objects.all()
	serializer_class = ServicoSerializer

	def get_permissions(self):
		return (permissions.AllowAny(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			Servico.objects.create_servico(**serializer.validated_data)

			response = Response(serializer.validated_data, status = status.HTTP_201_CREATED)
			response['Access-Control-Allow-Origin'] = '*'
			response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

			return response

		return Response({
			'status': 'Bad request',
			'message': 'Servico nao pode ser inserido com os dados recebidos'
			}, status = status.HTTP_400_BAD_REQUEST)

class SistemaViewSet(viewsets.ModelViewSet):
	queryset = Sistema.objects.all()
	serializer_class = SistemaSerializer

	def get_permissions(self):
		return (permissions.AllowAny(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			Sistema.objects.create_sistema(**serializer.validated_data)

			response = Response(serializer.validated_data, status = status.HTTP_201_CREATED)
			response['Access-Control-Allow-Origin'] = '*'
			response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

			return response

		return Response({
			'status': 'Bad request',
			'message': 'Sistema nao pode ser inserido com os dados recebidos'
			}, status = status.HTTP_400_BAD_REQUEST)

class KitDeplecaoViewSet(viewsets.ModelViewSet):
	queryset = KitDeplecao.objects.all()
	serializer_class = KitDeplecaoSerializer

	def get_permissions(self):
		return (permissions.AllowAny(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			KitDeplecao.objects.create_kit_deplecao(**serializer.validated_data)

			response = Response(serializer.validated_data, status = status.HTTP_201_CREATED)
			response['Access-Control-Allow-Origin'] = '*'
			response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

			return response

		return Response({
			'status': 'Bad request',
			'message': 'Kit Deplecao nao pode ser inserido com os dados recebidos'
			}, status = status.HTTP_400_BAD_REQUEST)

class InstituicaoViewSet(viewsets.ModelViewSet):
	queryset = Instituicao.objects.all()
	serializer_class = InstituicaoSerializer

	def get_serializer_class(self):
		return self.serializer_class


class ProjetoViewSet(viewsets.ModelViewSet):
	queryset = Projeto.objects.all()
	serializer_class = ProjetoSerializer

	def get_queryset(self):
		queryset = Projeto.objects.all()
		user = self.request.query_params.get('user', None)
		if user is not None:
			queryset = queryset.filter(usuarioprojetos__id=user)
		return queryset

	def get_serializer_class(self):
		if self.request.method == 'GET':
			return ProjetoReadSerializer
		else:
			return self.serializer_class



class UsuarioProjetoViewSet(viewsets.ModelViewSet):
	queryset = UsuarioProjeto.objects.all()
	serializer_class = UsuarioProjetoSerializer

	def get_serializer_class(self):
		return self.serializer_class

class ProjetoAmostraViewSet(viewsets.ModelViewSet):
	queryset = ProjetoAmostra.objects.all()
	serializer_class = ProjetoAmostraSerializer

	def get_serializer_class(self):
		return self.serializer_class

class PapelProjetoViewSet(viewsets.ModelViewSet):
	queryset = PapelProjeto.objects.all()
	serializer_class = PapelProjetoSerializer

class AmostraViewSet(viewsets.ModelViewSet):
	queryset = Amostra.objects.all()
	serializer_class = AmostraSerializer
	def get_serializer_class(self):
		if self.request.method == 'GET':
		 	return AmostraReadSerializer
		else:
			return self.serializer_class


class CorridaViewSet(viewsets.ModelViewSet):
	queryset = Corrida.objects.all()
	serializer_class = CorridaSerializer

	def get_serializer_class(self):
		if self.request.method == 'GET':
		 	return CorridaReadSerializer
		else:
			return self.serializer_class

class AmostraCorridaViewSet(viewsets.ModelViewSet):
	queryset = AmostraCorrida.objects.all()
	serializer_class = AmostraCorridaSerializer

	def get_serializer_class(self):
		if self.request.method == 'GET':
		 	return AmostraCorridaReadSerializer
		else:
			return self.serializer_class