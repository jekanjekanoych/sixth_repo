# Generated by Django 4.2.1 on 2023-05-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("group_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="teacher",
            name="age",
            field=models.IntegerField(max_length=200),
        ),
    ]
