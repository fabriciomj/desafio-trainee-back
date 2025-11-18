from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):  # noqa: ARG002
        return obj.owner == request.user


class IsAuthenticatedReadOnly(permissions.BasePermission):
    """Permissão que permite leitura de objetos para usuários autenticados."""

    def has_object_permission(self, request, view, obj):  # noqa: ARG002
        return (
            request.method in permissions.SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        )
