# Generated by Django 4.2.3 on 2023-09-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0004_hobbyfactor_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='season_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seasonname', models.CharField(max_length=20)),
            ],
        ),
    ]