# Generated by Django 4.2.3 on 2023-10-07 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_contact_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='blocklist_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('Remark', models.CharField(max_length=20)),
                ('Contactid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contactid', to='user.register_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]
