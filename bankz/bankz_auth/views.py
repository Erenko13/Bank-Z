
from .serializers import BankzObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication 

from bankz_auth.models import BankZUserParent, BankZUserChild, CashAccount


#? AUTHENTICATON ?#
class BankzObtainTokenPairView(TokenObtainPairView):

    permission_classes = (AllowAny, )
    serializer_class = BankzObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class BankZAuthenticationView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):

        user = User.objects.get(username=request.user.username)

        try:
            bankz_user = BankZUserChild.objects.get(user=user)
        except Exception as e:
            bankz_user = BankZUserParent.objects.get(user=user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            bankz_account = CashAccount.objects.get(user=user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        content = {
            'username': bankz_user.user.username,
            'uuid': bankz_user.id,
            'balance': bankz_account.balance
        }

        return Response(content)

#? CASH ACCOUNT ?#
class CashAccountTransfer(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):

        user = User.objects.get(username=request.user.username)

        uuid = request.data.get('transfer_id')
        balance = request.data.get('balance')

        try:
            bankz_user = BankZUserParent.objects.get(user=user)
        except:
            return Response({'error': 'Unknown parent user!'}, status=status.HTTP_404_NOT_FOUND)

        try:
            child = BankZUserChild.objects.get(id=uuid)
            child_user = child.user
            if child.parent != bankz_user:
                return Response({'error': 'Sent id is not a child of user!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Id not match with any child!'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            cash_account = CashAccount.objects.get(user=user)
        except:
            return Response({'error': 'Parent has no cash account!'}, status=status.HTTP_404_NOT_FOUND)

        try:
            child_account = CashAccount.objects.get(user=child_user)
        except:
            return Response({'error': 'Child has no cash account!'}, status=status.HTTP_404_NOT_FOUND)
        
        if cash_account.balance < (balance + 0): # 0 is commision
            return Response({'error': 'Given balance is more then account balance!'}, status=status.HTTP_400_BAD_REQUEST)
        
        cash_account.balance -= balance
        cash_account.save()
        child_account.balance += balance
        child_account.save()

        content = {
            'from': bankz_user.id,
            'to': child.id,
            'balance': balance,
            'new_balance': cash_account.balance,
            'new_child_account_balance': child_account.balance
        }

        return Response(content, status=status.HTTP_200_OK)
