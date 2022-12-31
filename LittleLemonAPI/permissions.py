from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return IsAdminUser().has_permission(request, view) or request.user.groups.filter(name='Manager').exists()


class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Delivery Crew').exists()


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.method in SAFE_METHODS


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.count() == 0
