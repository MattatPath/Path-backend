# Generated by Django 2.2.12 on 2021-02-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_transaction_deposit_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='wallet_address',
            field=models.CharField(max_length=42, primary_key=True, serialize=False),
        ),
    ]
