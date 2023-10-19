from rest_framework import permissions

class DirectorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.user.is_superuser:
            return True
        elif request.method in ['PUT','PATCH'] and hasattr(request.user,'director'):
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        elif request.user.is_superuser:
            return True
        elif request.method in ['PUT','PATCH'] and request.user.director.studio == obj:
            return True
        else:
            return False