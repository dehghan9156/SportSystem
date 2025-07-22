from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsRaceManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.role in ["admin","race_manager"]:
            return True
        return False
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in ["admin","race_manager"]:
            return True
        return False

class IsDovar(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["admin","dovar"]:
            return True
        return False
    
    def has_permission(self, request, view):
        if request.user.role in ["admin","dovar"]:
            return True
        return False
    
class IsRacer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["admin","racer"]:
            return True
        return False
    
    def has_permission(self, request, view):
        if request.user.role in ["admin","racer"]:
            return True
        return False