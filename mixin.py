from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class LoginRequiredMixin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        # Must be authenticated to view
        if request.user is None:
            return False

        return request.user.is_authenticated


class AllowModifyOnlyAuthorUserMixin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method == 'GET':
            return True

        if not request.user.is_authenticated:
            return False

        qs = User.objects.filter(email=request.user.email)
        if qs.exists():
            user = qs.get()
            return obj.author_id == user.id

        return False
