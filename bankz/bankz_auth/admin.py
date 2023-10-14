from django.contrib import admin
import bankz_auth.models as models

# Register your models here.
admin.site.register(models.BankZUserParent)
admin.site.register(models.BankZUserChild)
