# Generated by Django 4.0.2 on 2023-04-17 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_account', '0006_cashtransaction_from_name_cashtransaction_to_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashtransaction',
            name='balance',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cashtransaction',
            name='from_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cashtransaction',
            name='from_uuid',
            field=models.UUIDField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cashtransaction',
            name='to_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cashtransaction',
            name='to_uuid',
            field=models.UUIDField(default=None, null=True),
        ),
    ]
