# Generated by Django 5.0.6 on 2024-05-15 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "MOI_Assistant",
            "0003_rename_viechle_registration_consumers_vehicle_registration_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="consumers",
            name="vehicle_registration_expiry_date",
            field=models.DateField(default="2021-12-12"),
        ),
    ]
