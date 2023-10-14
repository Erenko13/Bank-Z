
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

from bankz_auth.models import BankZUserParent, BankZUserChild
from cash_account.models import CashAccount


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

        isParent = None

        try:
            bankz_user = BankZUserChild.objects.get(user=user)
            isParent = False
        except Exception as e:
            bankz_user = BankZUserParent.objects.get(user=user)
            isParent = True
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            bankz_account = CashAccount.objects.get(user=user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        relatives = []

        try:
            if isParent:
                for child in BankZUserChild.objects.filter(parent=bankz_user):
                    relatives.append({'username': child.user.username, 'uuid': child.id})
            else:
                relatives.append({'username': bankz_user.parent.user.username, 'uuid': bankz_user.parent.id})
        except:
            pass

        content = {
            'username': bankz_user.user.username,
            'uuid': bankz_user.id,
            'balance': bankz_account.balance,
            'relatives': relatives,
        }

        return Response(content)
