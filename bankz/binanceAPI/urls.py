
from django.urls import path
from binanceAPI.views import BinancePublic


urlpatterns = [
    path('public/<str:type>/', BinancePublic.as_view(), name='binance'),
    path('public/<str:type>/<str:symbol>', BinancePublic.as_view(), name='binance_exchangeInfo'),
]