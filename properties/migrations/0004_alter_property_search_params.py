# Generated by Django 5.0.6 on 2024-07-06 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0003_alter_property_search_params"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="search_params",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="properties.searchparams",
            ),
        ),
    ]
