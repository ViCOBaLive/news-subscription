# Generated by Django 4.1.7 on 2023-06-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="username", field=models.CharField(max_length=12),
        ),
    ]
