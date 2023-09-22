from rest_framework import permissions

from django.conf import settings

"""
SAFE_METHODS: GET, OPTIONS, HEAD
UNSAFE METHODS: POST, PUT, PATCH
"""


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET request for all users (authenticated and unauthenticated)
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True

        # Allow POST, PUT, and PATCH requests only for admin users (superuser)
        return request.user.is_superuser
