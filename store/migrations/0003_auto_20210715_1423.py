# Generated by Django 3.2.3 on 2021-07-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210627_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_percentage',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='offer_price',
            field=models.FloatField(null=True),
        ),
    ]