# Generated by Django 5.0.6 on 2024-06-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_availabledesign'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabledesign',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Product_Images'),
        ),
    ]
