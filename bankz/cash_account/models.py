
import uuid
from django.db import models
from django.contrib.auth.models import User

class CashAccount(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):

        return f'{self.user.username} - {self.balance}'
    
class CashTransaction(models.Model):

    STATUS_ERROR = 'error'
    STATUS_ONGOING = 'ongoing'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELED = 'cancelled'

    STATUS = [
        (STATUS_ERROR, 'Error!'),
        (STATUS_ONGOING, 'Ongoing...'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELED, 'Canceled!')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    from_name = models.CharField(max_length=255, default=None, null=True)
    to_name = models.CharField(max_length=255, default=None, null=True)
    
    from_uuid = models.UUIDField(default=None, null=True)
    to_uuid = models.UUIDField(default=None, null=True)
    balance = models.FloatField(default=0, null=True)

    status = models.CharField(max_length=100, choices=STATUS, default=STATUS_ONGOING)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f'[{self.status}] {self.from_name} -> {self.to_name} : {self.balance}'