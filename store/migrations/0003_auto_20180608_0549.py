# Generated by Django 2.0.4 on 2018-06-08 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.PositiveIntegerField(),
        ),
    ]
