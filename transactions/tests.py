from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from .models import Transaction
from .views import TransactionCreateView, TransactionListView, TransactionUpdateView, TransactionDeleteView, TransactionBalanceView
from users.models import User
import json

# Create your tests here.
class UserTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.incomeTransactionData = {
            'title': 'Salário',
            'type': 'income',
            'amount': 4000,
            'description': 'Minha principal fonte de renda.',
            'periodicity': 'monthly'
        }
        self.expenseTransactionData = {
            'title': 'Aluguel',
            'type': 'expense',
            'amount': 1400,
            'description': 'Aluguel do apartamento.',
            'periodicity': 'monthly'
        }
        self.user = User.objects.create_user({
            'username': 'beltrano',
            'email': 'beltrano@gmail.com',
            'password': '1357'
        })


    def testTransactionCreation(self):
        view = TransactionCreateView.as_view()

        request = self.factory.post('/transactions/create/', self.incomeTransactionData, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def testTransactionList(self):
        transaction = Transaction.objects.create(user=self.user, **self.incomeTransactionData)
        view = TransactionListView.as_view()

        request = self.factory.get('/transactions/list/')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def testTransactionUpdate(self):
        transaction = Transaction.objects.create(user=self.user, **self.incomeTransactionData)
        view = TransactionUpdateView.as_view()

        request = self.factory.patch(f'/transactions/update/{transaction.id}/', {'title': 'Freelance'}, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, id=transaction.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Freelance')

    def testTransactionDelete(self):
        transaction = Transaction.objects.create(user=self.user, **self.incomeTransactionData)
        view = TransactionDeleteView.as_view()

        request = self.factory.delete(f'/transactions/delete/{transaction.id}/')
        force_authenticate(request, user=self.user)
        response = view(request, id=transaction.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def testTransactionBalance(self):
        Transaction.objects.create(user=self.user, **self.incomeTransactionData)
        Transaction.objects.create(user=self.user, **self.expenseTransactionData)
        view = TransactionBalanceView.as_view()

        request = self.factory.get('/transactions/balance/')
        force_authenticate(request, user=self.user)
        response = view(request)

        content = json.loads(response.content)

        monthly_balance = content['monthlyBalance']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(monthly_balance, 2600)