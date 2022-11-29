# Generated by Django 3.2.13 on 2022-07-28 22:48

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
        (
            "wagtailpages",
            "0039_buyersguidearticlepage_buyersguideeditorialcontentindexpage",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="BuyersGuideContentCategory",
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
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, max_length=100, unique=True)),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "verbose_name": "Buyers Guide Content Category",
                "verbose_name_plural": "Buyers Guide Content Categories",
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
    ]
