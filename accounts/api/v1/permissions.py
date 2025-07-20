from rest_framework.permissions import BasePermission, SAFE_METHODS

class RaceManagerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["admin","race_manager"]:
            return True
        return False
    
    def has_permission(self, request, view):
        if request.user.role in ["admin","race_manager"]:
            return True
        return False

class DovarPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["admin","dovar"]:
            return True
        return False
    
    def has_permission(self, request, view):
        if request.user.role in ["admin","dovar"]:
            return True
        return False
    
class RacerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["admin","racer"]:
            return True
        return False
    
    def has_permission(self, request, view):
        if request.user.role in ["admin","racer"]:
            return True
        return False