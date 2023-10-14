
from django.contrib.auth.models import User
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bankz_auth.models import BankZUserParent, BankZUserChild
from cash_account.models import CashAccount, CashTransaction

#TODO: create transfer function
#TODO: make transfer any to any

#? CASH ACCOUNT ?#
#! transfer parent to child (CHANGE!)
class CashAccountTransfer(APIView):

    permission_classes = (IsAuthenticated, )

    def transferErrorHandler(self, transfer: CashTransaction):

        transfer.status = transfer.STATUS_ERROR
        transfer.save()

    def post(self, request):

        user = User.objects.get(username=request.user.username)

        uuid = request.data.get('uuid')
        balance = request.data.get('balance')

        new_transfer = CashTransaction()
        new_transfer.from_name = user.username
        new_transfer.balance = balance
        new_transfer.status = new_transfer.STATUS_ONGOING
        new_transfer.save()

        try:
            bankz_user = BankZUserParent.objects.get(user=user)
        except:
            self.transferErrorHandler(new_transfer)
            return Response({'error': 'Unknown parent user!'}, status=status.HTTP_404_NOT_FOUND)

        try:
            child = BankZUserChild.objects.get(id=uuid)
            child_user = child.user

            new_transfer.to_name = child_user.username

            if child.parent != bankz_user:
                self.transferErrorHandler(new_transfer)
                return Response({'error': 'Sent id is not a child of user!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            self.transferErrorHandler(new_transfer)
            return Response({'error': 'Id not match with any child!'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            cash_account = CashAccount.objects.get(user=user)
            new_transfer.from_uuid = cash_account.id
        except:
            self.transferErrorHandler(new_transfer)
            return Response({'error': 'Parent has no cash account!'}, status=status.HTTP_404_NOT_FOUND)

        try:
            child_account = CashAccount.objects.get(user=child_user)
            new_transfer.to_uuid = child_account.id
        except:
            self.transferErrorHandler(new_transfer)
            return Response({'error': 'Child has no cash account!'}, status=status.HTTP_404_NOT_FOUND)
        
        if balance <= 0:
            self.transferErrorHandler(new_transfer)
            return Response({'error': 'Given balance can\'t blow or equal to zero!'}, status=status.HTTP_400_BAD_REQUEST)
        
        if cash_account.balance < (balance + 0): # 0 is commision
            self.transferErrorHandler(new_transfer)
            return Response({'error': 'Given balance is more then account balance!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cash_account.balance -= balance
            cash_account.save()
            child_account.balance += balance
            child_account.save()
            new_transfer.status = new_transfer.STATUS_COMPLETED
            new_transfer.save()
        except:
            self.transferErrorHandler(new_transfer)

        #TODO: Cancel transfer

        content = {
            'from': bankz_user.id,
            'to': child.id,
            'balance': balance,
            'new_balance': cash_account.balance,
            'new_child_account_balance': child_account.balance
        }

        return Response(content, status=status.HTTP_200_OK)