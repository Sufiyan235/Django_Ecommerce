# Generated by Django 5.0.6 on 2024-06-26 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_country_account_state_account_zip_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='country',
        ),
        migrations.RemoveField(
            model_name='account',
            name='state',
        ),
        migrations.RemoveField(
            model_name='account',
            name='zip_code',
        ),
    ]
