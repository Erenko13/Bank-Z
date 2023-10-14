# Generated by Django 4.0.2 on 2023-04-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_account', '0002_cashtransactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashtransactions',
            name='status',
            field=models.CharField(choices=[('Error!', 'error'), ('Ongoing...', 'ongoing'), ('Completed', 'completed'), ('Canceled!', 'canceled')], default='Error!', max_length=100),
        ),
    ]
