# Generated by Django 4.2.3 on 2023-10-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0007_seasoncountry_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasoncountry_tb',
            name='Month',
            field=models.IntegerField(),
        ),
    ]