# Generated by Django 4.0.5 on 2022-06-09 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("online", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("nome", models.CharField(max_length=50)),
                ("historia", models.TextField()),
                ("foto", models.URLField()),
            ],
            options={
                "verbose_name": "Pet",
                "verbose_name_plural": "Pets",
            },
        ),
    ]
