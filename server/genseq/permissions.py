from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, usuario):
		if  request.user:
			return usuario == request.user
		return False