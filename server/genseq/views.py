# coding=UTF-8

import json

from django.contrib.auth import authenticate, login, logout

from rest_framework import status, views, permissions, viewsets
from rest_framework.response import Response

from genseq.permissions import IsAccountOwner
from genseq.models import Usuario, Servico, Sistema, KitDeplecao
from genseq.serializers import UsuarioSerializer, ServicoSerializer, SistemaSerializer, KitDeplecaoSerializer


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
	print('ONLOGOUT')
	permission_classes = (permissions.IsAuthenticated,)
	print('AFTERPERMS')

	def post(self, request, format=None):
		print('ONPOST')
		logout(request)

		return Response({}, status = status.HTTP_204_NO_CONTENT)

class ServicoViewSet(viewsets.ModelViewSet):
	queryset = Servico.objects.all()
	serializer_class = ServicoSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

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
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

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
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

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

