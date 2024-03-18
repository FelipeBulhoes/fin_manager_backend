from django.urls import path

from .views import TransactionCreateView, TransactionListView, TransactionUpdateView, TransactionDeleteView, TransactionBalanceView

urlpatterns = [
    path("create/", TransactionCreateView.as_view(), name="create"),
    path("list/", TransactionListView.as_view(), name="list"),
    path("update/<str:id>/", TransactionUpdateView.as_view(), name="update"),
    path("delete/<str:id>/", TransactionDeleteView.as_view(), name="delete"),
    path("balance/", TransactionBalanceView.as_view(), name="balance"),
]