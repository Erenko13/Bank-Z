
import uuid
from django.db import models
from django.contrib.auth.models import User
from cash_account.models import CashAccount

class BankZUserParent(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accounts = models.ManyToManyField(CashAccount, blank=True)

    def __str__(self):

        return self.user.username

class BankZUserChild(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(BankZUserParent, on_delete=models.SET_DEFAULT, default=None, null=True)
    accounts = models.ManyToManyField(CashAccount, blank=True)

    def __str__(self):

        return self.user.username