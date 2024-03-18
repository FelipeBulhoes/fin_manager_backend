from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Transaction

class OwnContentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        id = request.parser_context['kwargs'].get('id')

        if id is None:
            return False

        try:
            targetTransaction = Transaction.objects.get(id=id)
            return request.user.id == targetTransaction.user.id
        except Transaction.DoesNotExist:
            return False   