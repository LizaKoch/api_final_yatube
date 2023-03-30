from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorHasChangePermission(BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj) -> bool:
        del view
        if request.method in SAFE_METHODS or request.user == obj.author:
            return True
        return obj.author == request.user
