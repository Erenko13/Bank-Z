
from django.urls import path
from cash_account.views import CashAccountTransfer

urlpatterns = [
    path('transfer/', CashAccountTransfer.as_view(), name='trasfer'),
]