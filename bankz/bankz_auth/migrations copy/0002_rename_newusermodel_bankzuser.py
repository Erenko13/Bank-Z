# Generated by Django 4.0.2 on 2022-12-09 18:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankz_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewUserModel',
            new_name='BankZUser',
        ),
    ]