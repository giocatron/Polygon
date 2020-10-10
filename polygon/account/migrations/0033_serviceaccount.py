# Generated by Django 2.2.4 on 2019-09-05 10:10

import django.contrib.postgres.fields.jsonb
import oauthlib.common
from django.db import migrations, models

import polygon.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("account", "0032_remove_user_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceAccount",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "private_meta",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True,
                        default=dict,
                        encoder=polygon.core.utils.json_serializer.CustomJsonEncoder,
                        null=True,
                    ),
                ),
                (
                    "meta",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True,
                        default=dict,
                        encoder=polygon.core.utils.json_serializer.CustomJsonEncoder,
                        null=True,
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                (
                    "auth_token",
                    models.CharField(
                        default=oauthlib.common.generate_token,
                        max_length=30,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this service.",
                        related_name="service_set",
                        related_query_name="service",
                        to="auth.Permission",
                        verbose_name="service account permissions",
                    ),
                ),
            ],
            options={
                "permissions": (("manage_service_accounts", "Manage service account"),)
            },
        )
    ]
