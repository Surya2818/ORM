# Generated by Django 5.1.2 on 2024-11-16 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loan", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankloan",
            name="cust_name",
            field=models.CharField(max_length=100),
        ),
    ]
