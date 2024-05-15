from rest_framework import permissions
from django.contrib.auth.models import Group
from .models import User


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """

    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def is_in_group_admin(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return False
    except User.DoesNotExist:
        return False


class OwnerPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and request.user == obj.user


class HasGroupTLSVPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, "required_groups", {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        # Return True if the user has all the required groups or is staff.
        return all([is_in_group(request.user, group_name) if group_name != "__all__" else True for group_name in
                    required_groups]) or (request.user and request.user.is_staff)


class HasGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        u = User.objects.get(username=request.user.username)
        return is_in_group(u, "TLSV") or is_in_group(u, "CTSV") or u.is_staff

