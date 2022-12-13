# Generated by Django 4.1.4 on 2022-12-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankz_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankzuserchild',
            name='balance',
        ),
        migrations.AddField(
            model_name='bankzuserchild',
            name='accounts',
            field=models.ManyToManyField(blank=True, to='bankz_auth.cashaccount'),
        ),
        migrations.AlterField(
            model_name='bankzuserparent',
            name='accounts',
            field=models.ManyToManyField(blank=True, to='bankz_auth.cashaccount'),
        ),
    ]