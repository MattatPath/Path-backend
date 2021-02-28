# Generated by Django 2.2.12 on 2021-02-03 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default='0.00', max_length=20)),
                ('date', models.CharField(default='DATE', max_length=8)),
                ('identification', models.CharField(default='ID LENGTH?', max_length=20)),
                ('status', models.CharField(default='status pending', max_length=20)),
            ],
        ),
    ]
