# Generated by Django 4.2.3 on 2023-09-28 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0006_seasonfactor_tb'),
        ('user', '0004_rename_dob_register_tb_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='hobby_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hobbyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.hobbyname_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]
