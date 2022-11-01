
import requests
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

API_URL = 'https://api.binance.com/api/v3'


class BinancePublic(APIView):

    def get(self, request, type=None, symbol=None):

        if type is None:             return Response()
        elif type == 'ping':         return Response(self.ping())
        elif type == 'exchangeInfo': return Response(self.getExchangeInfo(symbol))


    def ping(self):
        
        try:
            return requests.get(API_URL + '/ping')
        except:
            return {'error': 'connection'}
    
    def getExchangeInfo(self, symbol=None):

        try:
            return requests.get(API_URL + f'/exchangeInfo?symbol={symbol}').json()
        except Exception as e:
            return {'error': 'connection'}


class BinancePrivate(APIView):

    def get(self, request, type=None, symbol=None):

        if type == None: return Response()
        elif type == 'login': return Response()