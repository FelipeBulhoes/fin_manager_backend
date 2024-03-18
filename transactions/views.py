from django.shortcuts import render
from .models import Transaction
from rest_framework.generics import (
    CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework import views
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TransactionSerializer
from .permissions import OwnContentPermission
from django.http import JsonResponse
# Create your views here.

class TransactionCreateView (CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        user_id = self.request.user.id
        serializer.save(user_id=user_id)

class TransactionListView (ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionUpdateView (UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, OwnContentPermission]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['patch']
    lookup_url_kwarg = 'id'

class TransactionDeleteView (DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, OwnContentPermission]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['delete']
    lookup_url_kwarg = 'id'


class TransactionBalanceView (views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        userId = request.user.id
        transactions = Transaction.objects.filter(user_id=userId)

        income = 0
        expense = 0

        for transaction in transactions:
            if transaction.type == 'income':
                if transaction.periodicity == 'yearly':
                    income += transaction.amount / 12
                else:
                    income += transaction.amount
            else:
                if transaction.periodicity == 'yearly':
                    expense += transaction.amount / 12
                else:
                    expense += transaction.amount

        monthlyBalance = income - expense
        yearlyBalance = monthlyBalance * 12

        insights = {
            'monthlyIncome': float(income),
            'monthlyExpense': float(expense),
            'monthlyBalance': float(monthlyBalance),
            'yearlyBalance': float(yearlyBalance)
        }
        
        return JsonResponse(insights)