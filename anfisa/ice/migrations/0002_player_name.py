# Generated by Django 5.1.1 on 2024-09-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ice", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="name",
            field=models.CharField(default="name", max_length=100),
        ),
    ]
