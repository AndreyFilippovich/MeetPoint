from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    '''Если пользователь не авторизован, то он может только смотреть.
    '''
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Разрешает действия с постами, только если ты владелец.
    В противном случае допускает только к просмотру.
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
