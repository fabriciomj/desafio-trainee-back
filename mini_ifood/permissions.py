from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwnerOrAuthenticated(permissions.BasePermission):
    """Permissão que permite ao owner de um objeto editá-lo e aos usuários autenticados visualizá-lo."""

    def has_object_permission(self, request, view, obj):
        if (
            request.method in permissions.SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ):
            return True

        return obj.owner == request.user
