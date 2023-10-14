
from django.contrib import admin
from cash_account import models

admin.site.register(models.CashAccount)
admin.site.register(models.CashTransaction)
