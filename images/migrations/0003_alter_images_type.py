# Generated by Django 3.2.9 on 2021-11-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='type',
            field=models.CharField(choices=[('encrypt_cbc', 'Encrypt_CBC'), ('decrypt_cbc', 'Decrypt_CBC'), ('encrypt_ecb', 'Encrypt_ECB'), ('decrypt_ecb', 'Decrypt_ECB')], max_length=40),
        ),
    ]
