
from django.urls import path
from bankz_auth.views import BankzObtainTokenPairView, RegisterView, BankZAuthenticationView, CashAccountTransfer
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('token/', BankzObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('getInfo/', BankZAuthenticationView.as_view(), name='getInfo'),
    path('transfer/', CashAccountTransfer.as_view(), name='trasfer'),
]