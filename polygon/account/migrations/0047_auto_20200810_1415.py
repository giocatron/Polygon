# Generated by Django 3.1 on 2020-08-10 14:15

from django.db import migrations, models

import polygon.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0046_user_jwt_token_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerevent",
            name="parameters",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=polygon.core.utils.json_serializer.CustomJsonEncoder,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=polygon.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="private_metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=polygon.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
    ]
