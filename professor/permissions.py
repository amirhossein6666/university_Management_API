from rest_framework import permissions

class Is_professor(permissions.BasePermission):
    def has_permission(self , request, view):
        return request.user.role == "professor"