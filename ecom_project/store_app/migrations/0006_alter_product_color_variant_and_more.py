# Generated by Django 5.0.6 on 2024-06-21 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_colorvariant_sizevariant_product_color_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_variant',
            field=models.ManyToManyField(blank=True, to='store_app.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='store_app.sizevariant'),
        ),
    ]
