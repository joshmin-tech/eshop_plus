# Generated by Django 3.2.3 on 2021-06-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
