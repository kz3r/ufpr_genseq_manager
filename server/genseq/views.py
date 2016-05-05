from rest_framework import permissions, viewsets

from genseq.models import Usuario
from genseq.permissions import IsAccountOwner
from genseq.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permission.AllowAny(),)

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