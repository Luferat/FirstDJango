# Generated by Django 5.1.3 on 2024-11-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='re_password',
            field=models.CharField(max_length=255),
        ),
    ]
