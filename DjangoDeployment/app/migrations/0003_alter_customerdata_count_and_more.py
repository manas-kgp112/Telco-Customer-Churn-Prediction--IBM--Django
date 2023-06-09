# Generated by Django 4.2.2 on 2023-06-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_customerdata_seniorcitizen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerdata",
            name="Count",
            field=models.IntegerField(choices=[(0, "0"), (1, "1")], null=True),
        ),
        migrations.AlterField(
            model_name="customerdata",
            name="SeniorCitizen",
            field=models.BooleanField(null=True),
        ),
    ]
